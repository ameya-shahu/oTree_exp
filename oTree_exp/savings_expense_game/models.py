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
    num_rounds = 25

    # define round at which emergency fund to shown
    # with emergency func amount
    emergedFund = {  # round : func
        4: 10000,
        12: 45000,
        19: 10000
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

            p.participant.vars['em'] = 0
            p.participant.vars['debt_2_round'] = 0
            p.participant.vars['debt_3_round'] = 0

            p.participant.vars['emi_1'] = 0
            p.participant.vars['emi_2'] = 0
            p.participant.vars['emi_3'] = 0

            p.participant.vars['savings_color'] = '#34ce57'


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
        choices=PLAYER_DEBTCHOICE_S,
    )

    fromSavingAmt = models.IntegerField(
        label=PLAYER_FROM_AMT_LABEL,
        blank=True
    )

    fromLoanAmount = models.IntegerField(
        label=PLAYER_LOAN_AMT_LABEL,
        blank=True
    )

    EMI1 = models.IntegerField(
        blank=True
    )

    EMI2 = models.IntegerField(
        blank=True
    )

    EMI3 = models.IntegerField(
        blank=True
    )
