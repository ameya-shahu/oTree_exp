from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

from .strings import *

author = 'github/ameya-shahu'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'saving_game_lite_hindi'
    players_per_group = None
    num_rounds = 16
    reqConsumption = 3000

    debtRound = [4, ]

    emergedFund = {
        debtRound[0]: 54000,
    }

    debtChoice = {
        debtRound[0]: [
            {'interest': 1.5, 'type': 'M', 'rounds': 10},
            {'interest': 8, 'type': 'Y', 'rounds': 12},
        ]
    }

    salaryFund = {
        1: 10000, 2: 10000, 3: 10000, 4: 10000, 5: 10000,
        6: 10000, 7: 10000, 8: 10000, 9: 10000, 10: 10000,
        11: 10000, 12: 10000, 13: 10000, 14: 10000, 15: 10000,
        16: 10000,
    }


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.participant.vars['totalSavings'] = 0
            p.participant.vars['homeSavings'] = 0
            p.participant.vars['bankSavings'] = 0
            p.participant.vars['totalDebt'] = 0
            p.participant.vars['EMI'] = 0
            p.participant.vars['loanRemainRound'] = 0


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # consumption variable
    consumption = models.IntegerField(label=PLAYER_CONSUMP_LABEL, min=Constants.reqConsumption)
    # savings at bank variable
    bankSavings = models.IntegerField(label=PLAYER_BANK_SAVING_LABEL,min=0)
    # savings at Home variable
    homeSavings = models.IntegerField(label=PLAYER_HOME_SAVING_LABEL,min=0)

    # cumulative home savings till this round
    cumBankSavings = models.IntegerField()

    # cumulative bank savings till this round
    cumHomeSavings = models.IntegerField()

    totalDebt = models.IntegerField()  # not in form

    EMI = models.IntegerField()

    fromLoanAmount = models.IntegerField(
        label=PLAYER_LOAN_AMT_LABEL,
        min=0
    )

    fromBankSavingAmt = models.IntegerField(
        label=PLAYER_FROM_BANK_AMT_LABEL,
        min=0
    )

    fromHomeSavingAmt = models.IntegerField(
        label=PLAYER_FROM_HOME_AMT_LABEL,
        min=0
    )

    debtChoice = models.StringField(
        label=PLAYER_DEBTCHOICE_LABEL,
        widget=widgets.RadioSelect,
    )

    def debtChoice_choices(self):
        debtOpt = Constants.debtChoice[self.round_number]
        choices = []
        for i, opt in enumerate(debtOpt):
            choice = [i,
                      PLAYER_DEBTCHOICE_S[1].format(opt["interest"], "मासिक (monthly)" if opt["type"] == "M" else "सालाना (yearly)",
                                                    opt["rounds"])]
            choices.append(choice)
        return choices




    # if less amount in bank savings
    def fromBankSavingAmt_error_message(self, value):
        if value > self.participant.vars['bankSavings']:
            return PG_DEBT_LESS_BANK_SAVE_ERROR

    def fromHomeSavingAmt_error_message(self, value):
        if value > self.participant.vars['homeSavings']:
            return PG_DEBT_LESS_HOME_SAVE_ERROR
