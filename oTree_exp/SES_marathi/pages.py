from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class SurveyFormBase(Page):
    template_name = 'SES_marathi/MyPage.html'
    form_model = 'player'

class hungerRate(SurveyFormBase):
    form_model = ['hungerRate ']

class tiredRate(SurveyFormBase):
    form_model = ['tiredRate']

class age(SurveyFormBase):
    form_model = ['age']

class gender(SurveyFormBase):
    form_model = ['gender']

class isMarried(SurveyFormBase):
    form_model = ['isMarried']

class religion(SurveyFormBase):
    form_model = ['religion']

class language(SurveyFormBase):
    form_model = ['language']

class education(SurveyFormBase):
    form_model = ['education']

class occupation(SurveyFormBase):
    form_model = ['occupation']

class useofhands(SurveyFormBase):
    form_model = ['useofhands']

class isOwnHouse(SurveyFormBase):
    form_model = ['isOwnHouse']

class hasbankaccount(SurveyFormBase):
    form_model = ['hasbankaccount']

class hasFD(SurveyFormBase):
    form_model = ['hasFD']

class hasmutualfunds(SurveyFormBase):
    form_model = ['hasmutualfunds']

class hasinsurance(SurveyFormBase):
    form_model = ['hasinsurance']

class gotcovid(SurveyFormBase):
    form_model = ['gotcovid']

class notnenoughfood(SurveyFormBase):
    form_model = ['notnenoughfood']

class howmanytimes(SurveyFormBase):
    form_model = ['howmanytimes']

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
                 notenoughfood,
                 howmanytimes
                 ]
