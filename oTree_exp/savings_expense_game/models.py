from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
    ExtraModel,
)

from .strings import *

author = 'github/ameya-shahu'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'savings_expense_game'
    players_per_group = None
    num_rounds = 16
    reqConsumption = 3000
    debtRound = [4,]
    # define round at which emergency fund to shown
    # with emergency func amount
    emergedFund = {  # round : func
        debtRound[0]: 54000,
        #debtRound[1]: 45000,
        #debtRound[2]: 2500
    }
    debtChoice = {
        debtRound[0]: [
            {'interest': 1.5, 'type': 'M', 'rounds': 10},
            {'interest': 8, 'type': 'Y', 'rounds': 12},
            # {'interest': 10, 'type': 'Y', 'rounds': 8},
        ],  # Y stands for yearly interest and M stands for monthly interest
        # debtRound[1]: [
        #     {'interest': 10, 'type': 'Y', 'rounds': 10},
        #     {'interest': 8, 'type': 'Y', 'rounds': 12},
        #     {'interest': 3, 'type': 'M', 'rounds': 12},
        # ],
        # debtRound[2]: [
        #     {'interest': 8, 'type': 'Y', 'rounds': 6},
        #     {'interest': 3, 'type': 'M', 'rounds': 6},
        #     {'interest': 10, 'type': 'Y', 'rounds': 3},
        # ],
    }

    salaryFund = {
        1: 10000, 2: 10000, 3: 10000, 4: 10000, 5: 10000,
        6: 10000, 7: 10000, 8: 10000, 9: 10000, 10: 10000,
        11: 10000, 12: 10000, 13: 10000, 14: 10000, 15: 10000,
        16: 10000, 17: 10000, 18: 10000, 19: 10000, 20: 10000,
        21: 10000, 22: 10000, 23: 10000, 24: 10000, 25: 10000,
    }


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.participant.vars['totalSavings'] = 0
            p.participant.vars['debts'] = list()
            p.participant.vars['totalDebt'] = 0

            p.participant.vars['debt_1_amount'] = 0
            p.participant.vars['debt_2_amount'] = 0
            p.participant.vars['debt_3_amount'] = 0

            p.participant.vars['debt_1_round'] = 0
            p.participant.vars['debt_2_round'] = 0
            p.participant.vars['debt_3_round'] = 0

            p.participant.vars['emi_1'] = 0
            p.participant.vars['emi_2'] = 0
            p.participant.vars['emi_3'] = 0

            p.participant.vars['debt_1_limit'] = 3
            p.participant.vars['debt_2_limit'] = 3
            p.participant.vars['debt_3_limit'] = 3

            p.participant.vars['savings_color'] = '#34ce57'

            p.participant.vars['set_warning'] = {
                'loan1Fault': False,
                'loan2Fault': False,
                'loan3Fault': False,
            }


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # consumption variable
    consumption = models.IntegerField(label=PLAYER_CONSUMP_LABEL)

    # savings variable
    savings = models.IntegerField(label=PLAYER_SAVING_LABEL)

    debtChoice = models.StringField(
        label=PLAYER_DEBTCHOICE_LABEL,
        widget=widgets.RadioSelect,
    )

    totalSavings = models.IntegerField()  # not to show on form
    totalDebts = models.IntegerField()  # not to show on form
    loan1Pending = models.IntegerField()  # not to show on form
    loan2Pending = models.IntegerField()  # not to show on form
    loan3Pending = models.IntegerField()  # not to show on form

    faultLoan1 = models.BooleanField()  # not to show on form
    faultLoan2 = models.BooleanField()  # not to show on form
    faultLoan3 = models.BooleanField()  # not to show on form

    fromSavingAmt = models.IntegerField(
        label=PLAYER_FROM_AMT_LABEL,
        blank=True
    )

    fromLoanAmount = models.IntegerField(
        label=PLAYER_LOAN_AMT_LABEL,
        blank=True
    )

    EMI1 = models.IntegerField()

    EMI2 = models.IntegerField()

    EMI3 = models.IntegerField()

    def debtChoice_choices(self):
        debtOpt = Constants.debtChoice[self.round_number]

        choices = [
            [0, PLAYER_DEBTCHOICE_S[0]],
        ]

        for i, opt in enumerate(debtOpt):
            choice = [i + 1,
                      PLAYER_DEBTCHOICE_S[1].format(opt["interest"], "मासिक" if opt["type"] == "M" else "वार्षिक",
                                                    opt["rounds"])]
            # choice = f'{opt["interest"]}% per {"Month" if opt["type"] == "M" else "Year"}, paid over {opt["rounds"]} rounds'
            choices.append(choice)

        return choices
