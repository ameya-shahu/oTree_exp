from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


# this class will define user-define template for all the questions and model
class SurveyFormBase(Page):
    template_name = 'depression_scale_marathi/MyPage.html'
    form_model = 'player'


'''all the classes below will use base class
as SurveyFormBase and use common template define by
SurveyFormBase. This will avoid to create all the template for individual
classes '''




class Sadness(SurveyFormBase):
    form_fields = ['sadness']


class Pessimistic(SurveyFormBase):
    form_fields = ['pessimistic']


class Setbacks(SurveyFormBase):
    form_fields = ['setbacks']


class LessJoy(SurveyFormBase):
    form_fields = ['lessJoy']


class Guilty(SurveyFormBase):
    form_fields = ['guilty']


# class ToBePunished(SurveyFormBase):
#     form_fields = ['toBePunished']


class SelfDoubt(SurveyFormBase):
    form_fields = ['selfDoubt']


# class SelfCriticism(SurveyFormBase):
#     form_fields = ['selfCriticism']


class Crying(SurveyFormBase):
    form_fields = ['crying']


# class Protest(SurveyFormBase):
#     form_fields = ['protest']


# class InterestLoss(SurveyFormBase):
#     form_fields = ['interestLoss']


class Uncertainty(SurveyFormBase):
    form_fields = ['uncertainty']


class Unemployment(SurveyFormBase):
    form_fields = ['unemployment']


# class LessEnergetic(SurveyFormBase):
#     form_fields = ['lessEnergetic']


# class SleepPattern(SurveyFormBase):
#     form_fields = ['sleepPattern']


# class Irritation(SurveyFormBase):
#     form_fields = ['irritation']


class Hunger(SurveyFormBase):
    form_fields = ['hunger']


class Concentration(SurveyFormBase):
    form_fields = ['concentration']


class Tiredness(SurveyFormBase):
    form_fields = ['tiredness']


'''default classes by oTree'''


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [
    Sadness,
    Pessimistic,
    Setbacks,
    LessJoy,
    Guilty,
    # ToBePunished,
    SelfDoubt,
    # SelfCriticism,
    Crying,
    # Protest,
    # InterestLoss,
    Uncertainty,
    Unemployment,
    # LessEnergetic,
    # SleepPattern,
    # Irritation,
    # Hunger,
    Concentration,
    # Tiredness,
    Results,
]
