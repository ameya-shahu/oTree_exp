from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


# this class will define user-define template for all the questions and model
class SurveyFormBase(Page):
    template_name = 'control_hindi/MyPage.html'
    form_model = 'player'


class doyouwatchbollywood(SurveyFormBase):
    form_fields = ['doyouwatchbollywood']


class favactor1(SurveyFormBase):
    form_fields = ['favactor1']


class favactor2(SurveyFormBase):
    form_fields = ['favactor2']


class favactor3(SurveyFormBase):
    form_fields = ['favactor3']


class favactor4(SurveyFormBase):
    form_fields = ['favactor4']


class favactor5(SurveyFormBase):
    form_fields = ['favactor5']


class favactress1(SurveyFormBase):
    form_fields = ['favactress1']


class favactress2(SurveyFormBase):
    form_fields = ['favactress2']


class favactress3(SurveyFormBase):
    form_fields = ['favactress3']


class favmovie1(SurveyFormBase):
    form_fields = ['favmovie1']


class favmovie2(SurveyFormBase):
    form_fields = ['favmovie2']


class favmovie3(SurveyFormBase):
    form_fields = ['favmovie3']


class doyoulikesongs(SurveyFormBase):
    form_fields = ['doyoulikesongs']


class favsinger1(SurveyFormBase):
    form_fields = ['favsinger1']


class favsinger2(SurveyFormBase):
    form_fields = ['favsinger2']


class favsinger3(SurveyFormBase):
    form_fields = ['favsinger3']


class favsinger4(SurveyFormBase):
    form_fields = ['favsinger4']


class favsinger5(SurveyFormBase):
    form_fields = ['favsinger5']


class favsinger6(SurveyFormBase):
    form_fields = ['favsinger6']


class music1990sor2000s(SurveyFormBase):
    form_fields = ['music1990sor2000s']


class sloworfastmusic(SurveyFormBase):
    form_fields = ['sloworfastmusic']


class doyouwatchtv(SurveyFormBase):
    form_fields = ['doyouwatchtv']


class onlineorontv(SurveyFormBase):
    form_fields = ['onlineorontv']


class lasttvshow(SurveyFormBase):
    form_fields = ['lasttvshow']


class howmuchyouliked(SurveyFormBase):
    form_fields = ['howmuchyouliked']


class optimistic(SurveyFormBase):
    form_fields = ['optimistic']


page_sequence = [doyouwatchbollywood,
                 favactor1, favactor2,
                 favactor3, favactor4, favactor5,
                 favactress1, favactress2, favactress3,
                 favmovie1, favmovie2, favmovie3,
                 doyoulikesongs,
                 favsinger1, favsinger2, favsinger3, favsinger4, favsinger5, favsinger6,
                 music1990sor2000s,
                 sloworfastmusic,
                 doyouwatchtv,
                 onlineorontv,
                 lasttvshow,
                 howmuchyouliked,
                 optimistic
                 ]
