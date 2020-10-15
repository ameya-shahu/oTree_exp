from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


# anything that has to be displayed goes into vars_for_template whereas internal calculations
# that do not need to be displayed go into before_next_page
# def is_displayed(self) is a condition on whether that page should be displayed or not - has
# nothing to do with internal calculations and shit

class Round1(Page):
    form_model = "player"
    form_fields = ['consumption_1' 'savings_1']

    def vars_for_template(self):
        self.player.total_savings_remaining = self.player.total_savings_remaining + self.player.savings_1
        return {
            "Total Savings:": self.player.total_savings_remaining
        }


class Round2(Page):
    form_model = "player"
    form_fields = ['consumption_2', 'savings_2']

    def vars_for_template(self):
        self.player.total_savings_remaining = self.player.total_savings_remaining + self.player.savings_2
        return {
            "Total Savings:": self.player.total_savings_remaining
        }


class Round3(Page):
    form_model = "player"
    form_fields = ['consumption_3', 'savings_3']


class Round4(Page):
    form_model = "player"
    form_fields = ['consumption_4', 'savings_4']


class Round5(Page):
    form_model = "player"
    form_fields = ['consumption_5', 'savings_5']


class Round6(Page):
    form_model = "player"
    form_fields = ['consumption_6', 'savings_6']


class Round7(Page):
    form_model = "player"
    form_fields = ['consumption_7', 'savings_7']


class Round8(Page):
    form_model = "player"
    form_fields = ['consumption_8', 'savings_8']


class Round9(Page):
    form_model = "player"
    form_fields = ['consumption_9', 'savings_9']


class Round10(Page):
    form_model = "player"
    form_fields = ['consumption_10', 'savings_10']


class Round11(Page):
    form_model = "player"
    form_fields = ['consumption_11', 'savings_11']


class Round12(Page):
    form_model = "player"
    form_fields = ['consumption_12', 'savings_12']


class Round13(Page):
    form_model = "player"
    form_fields = ['consumption_13', 'savings_13']


class Round14(Page):
    form_model = "player"
    form_fields = ['consumption_14', 'savings_14']


class Round15(Page):
    form_model = "player"
    form_fields = ['consumption_15', 'savings_15']


class Round16(Page):
    form_model = "player"
    form_fields = ['consumption_16', 'savings_16']


class Round17(Page):
    form_model = "player"
    form_fields = ['consumption_17', 'savings_17']


class Round18(Page):
    form_model = "player"
    form_fields = ['consumption_18', 'savings_18']


class Round19(Page):
    form_model = "player"
    form_fields = ['consumption_19', 'savings_19']


class Round20(Page):
    form_model = "player"
    form_fields = ['consumption_20', 'savings_20']


class Round21(Page):
    form_model = "player"
    form_fields = ['consumption_21', 'savings_21']


class Round22(Page):
    form_model = "player"
    form_fields = ['consumption_22', 'savings_22']


class Round23(Page):
    form_model = "player"
    form_fields = ['consumption_23', 'savings_23']


class Round24(Page):
    form_model = "player"
    form_fields = ['consumption_24', 'savings_25']


class Round25(Page):
    form_model = "player"
    form_fields = ['consumption_25', 'savings_25']


# class ResultsWaitPage(WaitPage):
#     pass


class Results(Page):
    form_fields = ['total_savings_remaining', 'total_debt_remaining', 'diff_between_savings_debt']


page_sequence = [MyPage, ResultsWaitPage, Results]
