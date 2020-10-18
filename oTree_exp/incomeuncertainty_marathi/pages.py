from ._builtin import Page, WaitPage


class SurveyFormBase(Page):
    template_name = 'incomeuncertainty_marathi/MyPage.html'
    form_model = 'player'


class HowManyPeople(SurveyFormBase):
    form_fields = ['howmanypeople']


class Howmanydependent(SurveyFormBase):
    form_fields = ['howmanydependent']


class Wenttoworktoday(SurveyFormBase):
    form_fields = ['wenttoworktoday']


class Wenttoworkbeforelockdown(SurveyFormBase):
    form_fields = ['wenttoworkbeforelockdown']


class Tempwork(SurveyFormBase):
    form_fields = ['tempwork']


class Areyouemployed(SurveyFormBase):
    form_fields = ['areyouemployed']


class Howmanymonthsago(SurveyFormBase):
    form_fields = ['howmanymonthsago']


class Directlylostjob(SurveyFormBase):
    form_fields = ['Directlylostjob']


class Fullorpartial(SurveyFormBase):
    form_fields = ['fullorpartial']


class Ifpartial(SurveyFormBase):
    form_fields = ['ifpartial']


class Otheremployed(SurveyFormBase):
    form_fields = ['otheremployed']


class Otherfullorpartial(SurveyFormBase):
    form_fields = ['otherfullorpartial']


class Otherifpartial(SurveyFormBase):
    form_fields = ['otherifpartial']


class Incomebeforelockdown(SurveyFormBase):
    form_fields = ['incomebeforelockdown']


class Incometoday(SurveyFormBase):
    form_fields = ['incometoday']


class Jobsecureorfinding(SurveyFormBase):
    form_fields = ['jobsecureorfinding']


class Lesssalary(SurveyFormBase):
    form_fields = ['lesssalary']


class Otherjobssecureorfinding(SurveyFormBase):
    form_fields = ['otherjobssecureorfinding']


class Otherlesssalary(SurveyFormBase):
    form_fields = ['otherlesssalary']


class Losejob3months(SurveyFormBase):
    form_fields = ['losejob3months']


class Otherskill(SurveyFormBase):
    form_fields = ['otherskill']


class Whatotherjob(SurveyFormBase):
    form_fields = ['whatotherjob']


class Willyougetone(SurveyFormBase):
    form_fields = ['willyougetone']


class Otherjobsalary(SurveyFormBase):
    form_fields = ['otherjobsalary']


class Standardofliving(SurveyFormBase):
    form_fields = ['standardofliving']


class Twojobs(SurveyFormBase):
    form_fields = ['twojobs']


class Competitiontofind(SurveyFormBase):
    form_fields = ['competitiontofind']


class Physicallywell(SurveyFormBase):
    form_fields = ['physicallywell']


class Covidhealth(SurveyFormBase):
    form_fields = ['covidhealth']


class Optimistic(SurveyFormBase):
    form_fields = ['optimistic']


class ResultsWaitPage(WaitPage):
    pass


page_sequence = [
    HowManyPeople,
    Howmanydependent,
    Wenttoworktoday,
    Wenttoworkbeforelockdown,
    Tempwork,
    Areyouemployed,
    Howmanymonthsago,
    Directlylostjob,
    Fullorpartial,
    Ifpartial,
    Otheremployed,
    Otherfullorpartial,
    Otherifpartial,
    Incomebeforelockdown,
    Incometoday,
    Jobsecureorfinding,
    Lesssalary,
    Otherjobssecureorfinding,
    Otherlesssalary,
    Losejob3months,
    Otherskill,
    Whatotherjob,
    Willyougetone,
    Otherjobsalary,
    Standardofliving,
    Twojobs,
    Competitiontofind,
    Physicallywell,
    Covidhealth,
    Optimistic
]