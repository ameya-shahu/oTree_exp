from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

ERROR_MSG = 'आपका उत्तर गलत है'


class SurveyFormBase(Page):
    template_name = 'instructions_quiz_hindi/MyPage.html'
    form_model = 'player'


class Instructionquestion1(SurveyFormBase):
    form_fields = ['instructionquestion1']

    def error_message(self, values):
        if values['instructionquestion1'] != 3:
            return ERROR_MSG


class Instructionquestion2(SurveyFormBase):
    form_fields = ['instructionquestion2']

    def error_message(self, values):
        if values['instructionquestion2'] != 2:
            return ERROR_MSG


class Instructionquestion3(SurveyFormBase):
    form_fields = ['instructionquestion3']

    def error_message(self, values):
        if values['instructionquestion3'] != 3:
            return ERROR_MSG


# class Instructionquestion4(SurveyFormBase):
#     form_fields = ['instructionquestion4']
#
#     def error_message(self, values):
#         if values['instructionquestion4'] != 3:
#             return ERROR_MSG
#
#
# class Instructionquestion5(SurveyFormBase):
#     form_fields = ['instructionquestion5']
#
#     def error_message(self, values):
#         if values['instructionquestion5'] != 2:
#             return ERROR_MSG
#
#
# class Instructionquestion6(SurveyFormBase):
#     form_fields = ['instructionquestion6']
#
#     def error_message(self, values):
#         if values['instructionquestion6'] != 2:
#             return ERROR_MSG
#
#
# class Instructionquestion7(SurveyFormBase):
#     form_fields = ['instructionquestion7']
#
#     def error_message(self, values):
#         if values['instructionquestion7'] != 2:
#             return ERROR_MSG
#
#
# class Instructionquestion8(SurveyFormBase):
#     form_fields = ['instructionquestion8']
#
#     def error_message(self, values):
#         if values['instructionquestion8'] != 2:
#             return ERROR_MSG
#

class Instructionquestion9(SurveyFormBase):
    form_fields = ['instructionquestion9']

    def error_message(self, values):
        if values['instructionquestion9'] != 3:
            return ERROR_MSG


class Results(Page):
    pass


page_sequence = [
    Instructionquestion1,
    Instructionquestion2,
    Instructionquestion3,
    # Instructionquestion4,
    # Instructionquestion5,
    # Instructionquestion6,
    # Instructionquestion7,
    # Instructionquestion8,
    Instructionquestion9,
    Results]
