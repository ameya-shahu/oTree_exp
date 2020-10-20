from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class SurveyFormBase(Page):
    template_name = 'hybrid_marathi/MyPage.html'
    form_model = 'player'


class howmanypeople(SurveyFormBase):
    form_fields = ['howmanypeople']


class howmanydependent(SurveyFormBase):
    form_fields = ['howmanydependent']


class wenttoworktoday(SurveyFormBase):
    form_fields = ['wenttoworktoday']


class tempwork(SurveyFormBase):
    form_fields = ['tempwork']


class wenttoworkbeforelockdown(SurveyFormBase):
    form_fields = ['wenttoworkbeforelockdown']


class areyouemployed(SurveyFormBase):
    form_fields = ['areyouemployed']


class howmanymonthsago(SurveyFormBase):
    form_fields = ['howmanymonthsago']


class directlylostjob(SurveyFormBase):
    form_fields = ['directlylostjob']


class fullorpartial(SurveyFormBase):
    form_fields = ['fullorpartial']


class jobsecureorfinding(SurveyFormBase):
    form_fields = ['jobsecureorfinding']


class lesssalary(SurveyFormBase):
    form_fields = ['lesssalary']


class losejob3months(SurveyFormBase):
    form_fields = ['losejob3months']


class current_conditions(SurveyFormBase):
    form_fields = ['current_conditions']


class howmuchpercentsavingsspent(SurveyFormBase):
    form_fields = ['howmuchpercentsavingsspent']


class howmuchleftsavings(SurveyFormBase):
    form_fields = ['howmuchleftsavings']


class doyouthinkthatisenough(SurveyFormBase):
    form_fields = ['doyouthinkthatisenough']


class otherskill(SurveyFormBase):
    form_fields = ['otherskill']


class whatotherjob(SurveyFormBase):
    form_fields = ['whatotherjob']


class willyougetone(SurveyFormBase):
    form_fields = ['willyougetone']


class standardofliving(SurveyFormBase):
    form_fields = ['standardofliving']


class celebratediwali(SurveyFormBase):
    form_fields = ['celebratediwali']


class howmuchcanyouspend(SurveyFormBase):
    form_fields = ['howmuchcanyouspend']


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


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [howmanypeople,
                 howmanydependent,
                 wenttoworktoday,
                 tempwork,
                 wenttoworkbeforelockdown,
                 areyouemployed,
                 howmanymonthsago,
                 directlylostjob,
                 fullorpartial,
                 jobsecureorfinding,
                 lesssalary,
                 losejob3months,
                 current_conditions,
                 howmuchpercentsavingsspent,
                 howmuchleftsavings,
                 doyouthinkthatisenough,
                 otherskill,
                 whatotherjob,
                 standardofliving,
                 celebratediwali,
                 emergency1000rupees,
                 emergency10000rupees,
                 emergency50000rupees,
                 emergency100000rupees,
                 emergency500000rupees,
                 optimistic,
                 Results,
                 ]
