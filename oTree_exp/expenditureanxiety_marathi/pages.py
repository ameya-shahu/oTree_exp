from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class SurveyFormBase(Page):
    template_name = 'expenditure_anxiety_marathi/MyPage.html'
    form_model = 'player'


'''all the classes below will use base class
as SurveyFormBase and use common template define by
SurveyFormBase. This will avoid to create all the template for individual
classes '''


class howmanypeople(SurveyFormBase):
    form_fields = ['howmanypeople']


class howmanydependent(SurveyFormBase):
    form_fields = ['howmanydependent']


class areyouemployed(SurveyFormBase):
    form_fields = ['areyouemployed']


class howmanymonthsago(SurveyFormBase):
    form_fields = ['howmanymonthsago']


class fullorpartial(SurveyFormBase):
    form_fields = ['fullorpartial']


class groceries_weekly(SurveyFormBase):
    form_fields = ['groceries_weekly']


class groceries_gonedown(SurveyFormBase):
    form_fields = ['groceries_gonedown']


class electricity_monthly(SurveyFormBase):
    form_fields = ['electricity_monthly']


class electricity_goneup(SurveyFormBase):
    form_fields = ['electricity_goneup']


class mobile_monthly(SurveyFormBase):
    form_fields = ['mobile_monthly'],


class mobile_goneup(SurveyFormBase):
    form_fields = ['mobile_goneup']


class current_conditions(SurveyFormBase):
    form_fields = ['current_conditions']


class unexpected_increase(SurveyFormBase):
    form_fields = ['unexpected_increase']


class savingsbeforelockdown(SurveyFormBase):
    form_fields = ['savingsbeforelockdown']


class howmuchpercentsavingsspent(SurveyFormBase):
    form_fields = ['howmuchpercentsavingsspent']


class howmuchleftsavings(SurveyFormBase):
    form_fields = ['howmuchleftsavings']


class doyouthinkthatisenough(SurveyFormBase):
    form_fields = ['doyouthinkthatisenough']


class celebratediwali(SurveyFormBase):
    form_fields = ['celebratediwali']


class whatwillyouspendon(SurveyFormBase):
    form_fields = ['whatwillyouspendon']


class howmuchcanyouspend(SurveyFormBase):
    form_fields = ['howmuchcanyouspend']


class enoughfoodfortwomeals(SurveyFormBase):
    form_fields = ['enoughfoodfortwomeals']


class howlongcanyouensurefood(SurveyFormBase):
    form_fields = ['howlongcanyouensurefood']


class emergency1000rupees(SurveyFormBase):
    form_fields = ['emergency1000rupees']


class emergency10000rupees(SurveyFormBase):
    form_fields = ['emergency10000rupees']


class emergency50000rupees(SurveyFormBase):
    form_fields = ['emergency50000rupees']


class emergency100000rupees(SurveyFormBase):
    form_fields = ['emergency100000rupees']


class emergency500000rupees(SurveyFormBase):
    form_fields = ['emergency500000rupees']


class optimistic(SurveyFormBase):
    form_fields = ['optimistic']


page_sequence = [howmanypeople,
                 howmanydependent,
                 areyouemployed,
                 howmanymonthsago,
                 fullorpartial,
                 groceries_weekly,
                 groceries_gonedown,
                 electricity_monthly,
                 electricity_goneup,
                 mobile_monthly,
                 mobile_goneup,
                 current_conditions,
                 unexpected_increase,
                 savingsbeforelockdown,
                 howmuchpercentsavingsspent,
                 howmuchleftsavings,
                 doyouthinkthatisenough,
                 celebratediwali,
                 whatwillyouspendon,
                 howmuchcanyouspend,
                 enoughfoodfortwomeals,
                 howlongcanyouensurefood,
                 emergency1000rupees,
                 emergency10000rupees,
                 emergency50000rupees,
                 emergency100000rupees,
                 emergency500000rupees,
                 optimistic]
