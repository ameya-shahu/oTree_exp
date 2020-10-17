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

author = 'aishdeshp'

doc = """
Savings Game 
"""


class Constants(BaseConstants):
    name_in_url = 'savings_game'
    players_per_group = None
    num_rounds = 4
    # endowment = 100000 - not a variable since this is just displayed and not manipulated


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # all consumption variables - 25 rounds, 25 variables
    consumption = models.IntegerField(label="खर्च :")

    # all savings variables - 25 rounds, 25 variables
    savings = models.IntegerField(label="बचत :")

    # cumulative savings variable - one that gets updated every round
    total_savings_remaining = models.IntegerField(label="एकूण शिल्लक बचत :")
    # total_savings_remaining = 0

    # the fun begins here - all the debt related variables

    # debt options for each expenditure round
    debt_option_round_4 = models.IntegerField(
        label="आपण कोणता पर्याय निवडत आहात?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "8% वार्षिक, परतफेडीचा कालावधी - 10 राऊंड्स"],
            [2, "10% वार्षिक, परतफेडीचा कालावधी - 8 राऊंड्स"]
        ])

    debt_option_round_12 = models.IntegerField(
        label="आपण कोणता पर्याय निवडत आहात?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "10% वार्षिक, परतफेडीचा कालावधी - 10 राऊंड्स"],
            [2, "8% वार्षिक, परतफेडीचा कालावधी - 12 राऊंड्स"],
            [3, "रीफायनान्स करुन 8% वार्षिक, रीफायनान्स करण्याची फी रु. 100 "]
        ])

    debt_option_round_19 = models.IntegerField(
        label="आपण कोणता पर्याय निवडत आहात?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "रीफायनान्स करुन 8% वार्षिक, रीफायनान्स करण्याची फी रु. 100"],
            [2, "नवीन रक्कम 8% वार्षिक, परतफेडीचा कालावधी - 6 राऊंड्स"],
            [3, "नवीन रक्कम 10% वार्षिक, परतफेडीचा कालावधी - 3 राऊंड्स"]
        ])

    # debt taken input value for each expenditure round
    debt_taken_round_4 = models.IntegerField(label="आपण किती कर्ज घेत आहात?")
    debt_taken_round_12 = models.IntegerField(label="आपण किती कर्ज घेत आहात?")
    debt_taken_round_19 = models.IntegerField(label="आपण किती कर्ज घेत आहात?")

    # debt amount with interest
    debt_amount_with_interest_round_4 = models.IntegerField(label="आपले व्याजासकट कर्ज इतके आहे :")
    debt_amount_with_interest_round_12 = models.IntegerField(label="आपले व्याजासकट कर्ज इतके आहे :")
    debt_amount_with_interest_round_19 = models.IntegerField(label="आपले व्याजासकट कर्ज इतके आहे :")

    # emi calculation
    debt_round4_emi = models.IntegerField(label="दर राऊंड चा हफ्ता आहे :")
    debt_round12_emi = models.IntegerField(label="दर राऊंड चा हफ्ता आहे :")
    debt_round19_emi = models.IntegerField(label="दर राऊंड चा हफ्ता आहे :")

    # need a variable to input the debt value in every round - right below the emi indication

    # remaining debt
    debt_round4_remaining = models.IntegerField(label="आपले इतके कर्ज शिल्लक आहे :")
    debt_round12_remaining = models.IntegerField(label="आपले इतके कर्ज शिल्लक आहे :")
    debt_round19_remaining = models.IntegerField(label="आपले इतके कर्ज शिल्लक आहे :")

    # remaining rounds for each debt

    debt_round4_rounds_remaining = models.IntegerField(label="परतफेडीचा कालावधी इतका शिल्लक आहे (राऊंड्स) :")
    debt_round12_rounds_remaining = models.IntegerField(label="परतफेडीचा कालावधी इतका शिल्लक आहे (राऊंड्स) :")
    debt_round19_rounds_remaining = models.IntegerField(label="परतफेडीचा कालावधी इतका शिल्लक आहे (राऊंड्स) :")

    # total debt remaining
    total_debt_remaining = models.IntegerField(label="एकूण शिल्लक कर्ज :")

    # difference between savings and debt
    diff_between_savings_debt = models.IntegerField(label="बचत आणि कर्ज यातील फरक :")
