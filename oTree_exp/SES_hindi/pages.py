from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class SurveyFormBase(Page):
    template_name = 'SES_hindi/MyPage.html'
    form_model = 'player'


class hungerRate(SurveyFormBase):
    form_fields = ['hungerRate']


class tiredRate(SurveyFormBase):
    form_fields = ['tiredRate']


class age(SurveyFormBase):
    form_fields = ['age']


class gender(SurveyFormBase):
    form_fields = ['gender']


class isMarried(SurveyFormBase):
    form_fields = ['isMarried']


class religion(SurveyFormBase):
    form_fields = ['religion']


class language(SurveyFormBase):
    form_fields = ['language']


class education(SurveyFormBase):
    form_fields = ['education']


class occupation(SurveyFormBase):
    form_fields = ['occupation']


class useofhands(SurveyFormBase):
    form_fields = ['useofhands']


class isOwnHouse(SurveyFormBase):
    form_fields = ['isOwnHouse']


class hasbankaccount(SurveyFormBase):
    form_fields = ['hasbankaccount']


class hasFD(SurveyFormBase):
    form_fields = ['hasFD']


class hasmutualfunds(SurveyFormBase):
    form_fields = ['hasmutualfunds']


class hasinsurance(SurveyFormBase):
    form_fields = ['hasinsurance']


class gotcovid(SurveyFormBase):
    form_fields = ['gotcovid']


class notnenoughfood(SurveyFormBase):
    form_fields = ['notnenoughfood']


class howmanytimes(SurveyFormBase):
    form_fields = ['howmanytimes']


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [hungerRate,
                 tiredRate,
                 age,
                 gender,
                 isMarried,
                 religion,
                 language,
                 education,
                 occupation,
                 useofhands,
                 isOwnHouse,
                 hasbankaccount,
                 hasFD,
                 hasmutualfunds,
                 hasinsurance,
                 gotcovid,
                 notnenoughfood,
                 howmanytimes,
                 Results,
                 ]
