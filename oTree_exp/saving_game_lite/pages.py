from otree.api import Currency as c, currency_range
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


def calculateLoan(amount, intrestPerRound, noOfRounds):
    intrestAmount = int((amount * intrestPerRound * noOfRounds) / 100)
    return intrestAmount + amount


def calculateEmi(loanAmount, rounds):
    try:
        return int(loanAmount / rounds)
    except ZeroDivisionError:
        return loanAmount


class MyPage(Page):
    form_model = 'player'

    def __init__(self):
        self.fieldList = ['consumption', 'bankSavings', 'homeSavings']

    def get_form_fields(self):
        if self.participant.vars['loanRemainRound'] > 0:  # if loan is there append EMI field
            self.fieldList.append('EMI')

        return self.fieldList

    def vars_for_template(self):
        # pass question depend on the round number
        return {
            'roundSalary': Constants.salaryFund[self.round_number],
        }

    def error_message(self, values):
        EMI = 0
        if 'EMI' in self.fieldList:
            if values['EMI'] > self.participant.vars['EMI']:
                return EMI_1_LABEL.format(self.participant.vars['EMI'])
            EMI += values['EMI']

        # sumation of all the fields in form
        fieldSum = (int(values['consumption']) +
                    int(values['bankSavings']) +
                    int(values['homeSavings']) +
                    int(EMI))

        if fieldSum > 10000:
            return PG_MY_FIELD_SUM_GREAT_ERROR
        elif fieldSum < 10000:
            return PG_MY_FIELD_SUM_LESS_ERROR

    def before_next_page(self):
        self.participant.vars['totalSavings'] += (int(self.player.homeSavings) + int(self.player.bankSavings))
        self.participant.vars['homeSavings'] += int(self.player.homeSavings)
        self.participant.vars['bankSavings'] += int(self.player.bankSavings)

        self.player.cumHomeSavings = self.participant.vars['homeSavings']
        self.player.cumBankSavings = self.participant.vars['bankSavings']

        print('home Svings - ', self.participant.vars['homeSavings'])
        print('bank Svings - ', self.participant.vars['bankSavings'])

        if 'EMI' in self.fieldList:
            self.participant.vars['totalDebt'] -= self.player.EMI
            self.participant.vars['loanRemainRound'] -= 1
            self.player.totalDebt = self.participant.vars['totalDebt']


class DebtChoicePage(Page):
    form_model = "player"
    form_fields = ['debtChoice', 'fromHomeSavingAmt', 'fromBankSavingAmt', 'fromLoanAmount']

    def vars_for_template(self):
        return {
            'emergedFund': Constants.emergedFund[self.round_number],
        }

    def is_displayed(self):
        return True if self.round_number in Constants.debtRound else False

    def error_message(self, values):
        # if sumation loan+from home + from bank is less or greater
        if (values['fromBankSavingAmt'] + values['fromBankSavingAmt'] + values['fromLoanAmount']) > \
                Constants.emergedFund[self.round_number]:
            return PG_DEBTCHOICE_LOANSUM_GREAT_ERROR.format(Constants.emergedFund[self.round_number])

        if (values['fromBankSavingAmt'] + values['fromBankSavingAmt'] + values['fromLoanAmount']) < \
                Constants.emergedFund[self.round_number]:
            return PG_DEBTCHOICE_LOANSUM_LESS_ERROR.format(Constants.emergedFund[self.round_number])

    def before_next_page(self):
        if self.is_displayed():
            choosenOpt = int(self.player.debtChoice)
            loanAmt = int(self.player.fromLoanAmount)
            if loanAmt > 0:
                debtDetails = Constants.debtChoice[self.round_number][
                    choosenOpt - 1]  # get details of debt from  Constants class

                interest = debtDetails['interest'] if debtDetails['type'] == 'M' else debtDetails[
                                                                                          'interest'] / 12  # calculate monthly intrest
                totalAmount = calculateLoan(loanAmt, interest, debtDetails['rounds'])
                self.participant.vars['totalDebt'] = totalAmount
                self.participant.vars['EMI'] = calculateEmi(totalAmount, debtDetails['rounds'])
                self.participant.vars['loanRemainRound'] = debtDetails['rounds']
                self.player.totalDebt = totalAmount

                self.participant.vars['totalSavings'] -= (int(self.player.fromBankSavingAmt) + int(self.player.fromHomeSavingAmt))
                self.participant.vars['homeSavings'] -= int(self.player.fromHomeSavingAmt)
                self.participant.vars['bankSavings'] -= int(self.player.fromBankSavingAmt)

                self.player.cumHomeSavings = self.participant.vars['homeSavings']
                self.player.cumBankSavings = self.participant.vars['bankSavings']




class Results(Page):
    def is_displayed(self):
        return Constants.num_rounds == self.round_number

    def vars_for_template(self):
        if self.is_displayed():
            return dict(
                diff=self.participant.vars['totalSavings'] - self.participant.vars['totalDebt'],
            )


page_sequence = [MyPage, DebtChoicePage, Results]
