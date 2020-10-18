from ._builtin import Page, WaitPage
from .models import Constants
from .strings import *


def emergedFundValidate(enteredAmt, round_no):
    if enteredAmt > Constants.emergedFund[round_no]:
        return PG_DEBTCHOICE_LOANSUM_GREAT_ERROR.format(Constants.emergedFund[round_no])
    elif enteredAmt < Constants.emergedFund[round_no]:
        return PG_DEBTCHOICE_LOANSUM_LESS_ERROR.format(Constants.emergedFund[round_no])
    else:
        return None


def salaryFundValidate(enteredAmt, round_no):
    if enteredAmt > Constants.salaryFund[round_no]:
        return PG_MY_FIELD_SUM_GREAT_ERROR
    elif enteredAmt < Constants.salaryFund[round_no]:
        return PG_MY_FIELD_SUM_LESS_ERROR
    else:
        return None


def calculateLoan(amount, intrestPerRound, noOfRounds):
    intrestAmount = int((amount * intrestPerRound * noOfRounds) / 100)
    return intrestAmount + amount


def calculateEmi(loanAmount, rounds):
    return int(loanAmount / rounds)


class MyPage(Page):
    form_model = "player"

    def __init__(self):
        self.fieldList = ['consumption', 'savings']

    def get_form_fields(self):

        if (self.participant.vars['debt_1_round'] > 0) and (self.participant.vars['debt_1_limit'] > 0):
            self.fieldList.append('EMI1')

        if (self.participant.vars['debt_2_round'] > 0) and (self.participant.vars['debt_2_limit'] > 0):
            self.fieldList.append('EMI2')

        if (self.participant.vars['debt_3_round'] > 0) and (self.participant.vars['debt_3_limit'] > 0):
            self.fieldList.append('EMI3')

        return self.fieldList

    def vars_for_template(self):
        # pass question depend on the round number
        return {
            'roundSalary': Constants.salaryFund[self.round_number],
        }

    def before_next_page(self):
        # add entered saving to cumulative savings variable
        self.participant.vars['totalSavings'] += int(self.player.savings)
        self.participant.vars['savings_color'] = '#34ce57'  # green color as savings increased

        reduceDebt = 0

        # verify EMIs
        if 'EMI1' in self.fieldList:
            self.participant.vars['debt_1_amount'] -= self.player.EMI1
            self.participant.vars['debt_1_round'] -= 1
            reduceDebt -= self.player.EMI1
            # if less than ideal emi paid by user then recalculate emi
            if self.player.EMI1 < self.participant.vars['emi_1']:
                self.participant.vars['emi_1'] = calculateEmi(self.participant.vars['debt_1_amount'],
                                                              self.participant.vars['debt_1_round'])
                self.participant.vars['debt_1_limit']-=1

        if 'EMI2' in self.fieldList:
            self.participant.vars['debt_2_amount'] -= self.player.EMI2
            self.participant.vars['debt_2_round'] -= 1
            reduceDebt -= self.player.EMI2
            if self.player.EMI2 < self.participant.vars['emi_2']:
                self.participant.vars['emi_2'] = calculateEmi(self.participant.vars['debt_2_amount'],
                                                              self.participant.vars['debt_2_round'])
                self.participant.vars['debt_2_limit'] -= 1

        if 'EMI3' in self.fieldList:
            self.participant.vars['debt_3_amount'] -= self.player.EMI3
            self.participant.vars['debt_3_round'] -= 1
            reduceDebt -= self.player.EMI3
            if self.player.EMI3 < self.participant.vars['emi_3']:
                self.participant.vars['emi_3'] = calculateEmi(self.participant.vars['debt_3_amount'],
                                                              self.participant.vars['debt_3_round'])
                self.participant.vars['debt_3_limit'] -= 1

        self.participant.vars['totalDebt'] -= int(reduceDebt)

    def error_message(self, values):
        # return error if cosume amount is less than set standard
        if values['consumption'] < Constants.reqConsumption:
            return PG_MY_CONSUME_LESS_ERROR.format(Constants.reqConsumption)

        # display error if sum of 'savings', 'consumption' and EMIs field is not exactly equal to round amount
        # also validate EMIs are less than equal to ideal EMI
        emiSum = 0
        if ('EMI1' in self.fieldList) and (values['EMI1'] > self.participant.vars['emi_1']):
            return EMI_1_LABEL.format(self.participant.vars['emi_1'])
        elif 'EMI1' in self.fieldList:
            emiSum += int(values['EMI1'])

        if ('EMI2' in self.fieldList) and (values['EMI2'] > self.participant.vars['emi_2']):
            return EMI_2_LABEL.format(self.participant.vars['emi_2'])
        elif 'EMI2' in self.fieldList:
            emiSum += int(values['EMI2'])

        if ('EMI3' in self.fieldList) and (values['EMI3'] > self.participant.vars['emi_3']):
            return EMI_3_LABEL.format(self.participant.vars['emi_3'])
        elif 'EMI3' in self.fieldList:
            emiSum += int(values['EMI3'])

        field_sum = (int(values['consumption']) + int(values['savings']) + int(emiSum))
        error = salaryFundValidate(field_sum, self.round_number)
        if error is not None:
            return error


class DebtChoicePage(Page):
    form_model = "player"
    form_fields = ['debtChoice', 'fromSavingAmt', 'fromLoanAmount']

    def vars_for_template(self):
        return {
            'emergedFund': Constants.emergedFund[self.round_number],
        }

    def is_displayed(self):
        return True if self.round_number in Constants.debtRound else False

    def error_message(self, values):
        # display error if expenditure is not totally spend from savings
        # and sum of amount withdrawal from savings and amount taken as loan is not equal to 10,000
        if int(values['debtChoice']) != 0:
            if self.participant.vars['totalSavings'] < values['fromSavingAmt']:
                return PG_DEBTCHOICE_LESS_SAVINGS_ERROR

            loanSaveSum = int(values['fromSavingAmt']) + int(values['fromLoanAmount'])
            error = emergedFundValidate(loanSaveSum, self.round_number)
            if error is not None:
                return error

        # if totalSavings is less than emergencyFund appeared, then return error.
        else:
            if self.participant.vars['totalSavings'] < Constants.emergedFund[self.round_number]:
                return PG_DEBTCHOICE_LESS_SAVINGS_ERROR

    def before_next_page(self):
        # if expenditure is chose as from totalSaving then set fromSavingAmt = emergencyFund
        if self.player.debtChoice == int(self.player.debtChoice):
            # at round when emergencyFund appear, set field related to it.
            self.player.fromSavingAmt = Constants.emergedFund[self.round_number]
            self.player.fromLoanAmount = 0

        # else create debt according selected option
        else:
            chooseOpt = int(self.player.debtChoice)
            loanAmt = int(self.player.fromLoanAmount)

            debtDetails = Constants.debtChoice[self.round_number][
                chooseOpt - 1]  # get details of debt from  Constants class
            interest = debtDetails['interest'] if debtDetails['type'] == 'M' else debtDetails[
                                                                                      'interest'] / 12  # calculate monthly intrest
            totalAmount = calculateLoan(loanAmt, interest, debtDetails['rounds'])

            print('[interest]-', interest)

            NewDebt = {
                'amountRemaining': totalAmount,
                'emiRoundRemaining': debtDetails['rounds'],
                'emiAmount': calculateEmi(totalAmount, debtDetails['rounds'])
            }

            print(NewDebt)

            self.setLoan(NewDebt)
            self.player.debtChoice = PLAYER_DEBTCHOICE_S[1].format(debtDetails["interest"],
                                                                   "Month" if debtDetails["type"] == "M" else "Year",
                                                                   debtDetails["rounds"])

            self.participant.vars['totalDebt'] += NewDebt['amountRemaining']

        # subtract 'fromSavingAmt' from cumulative totalSavings
        self.participant.vars['totalSavings'] -= self.player.fromSavingAmt
        self.participant.vars['savings_color'] = '#f50707'  # red color as savings decreased

    def setLoan(self, newDebt):
        if self.participant.vars['emi_1'] == 0:
            self.participant.vars['emi_1'] = newDebt['emiAmount']
            self.participant.vars['debt_1_amount'] = newDebt['amountRemaining']
            self.participant.vars['debt_1_round'] = newDebt['emiRoundRemaining']

        elif self.participant.vars['emi_2'] == 0:
            self.participant.vars['emi_2'] = newDebt['emiAmount']
            self.participant.vars['debt_2_amount'] = newDebt['amountRemaining']
            self.participant.vars['debt_2_round'] = newDebt['emiRoundRemaining']

        elif self.participant.vars['emi_3'] == 0:
            self.participant.vars['emi_3'] = newDebt['emiAmount']
            self.participant.vars['debt_3_amount'] = newDebt['amountRemaining']
            self.participant.vars['debt_3_round'] = newDebt['emiRoundRemaining']


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, DebtChoicePage, ]
