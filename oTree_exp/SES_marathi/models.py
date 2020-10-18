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

from django import forms

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'SES_marathi'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


yesNoChoice = [
    [True, 'होय'],
    [False, 'नाही'],
]


class Player(BasePlayer):
    hungerRate = models.IntegerField(
        label='प्रयोगादरम्यान आपल्याला किती भूक लागली होती ते रेटिंग द्या (1 ते 5)',
        min=1,
        max=5,
    )

    tiredRate = models.IntegerField(
        label='प्रयोगादरम्यान आपण किती थकलेले आहात त्याचे रेटिंग द्या (1 ते 5)',
        min=1,
        max=5
    )

    age = models.IntegerField(
        label='तुमचे वय काय आहे?'
    )

    gender = models.StringField(
        label='तुमचे लिंग काय आहे?',
        widget=widgets.RadioSelect,
        choices=[
            ['Male', 'पुरुष'],
            ['female', 'महिला']
        ],
    )

    isMarried = models.BooleanField(
        label='तुमचे लग्न झाले आहे का?',
        widget=widgets.RadioSelect,
        choices=yesNoChoice
    )

    religion = models.StringField(
        label='तुमचे धर्म कोणता?',
        choices=[
            ['Hinduism', 'हिंदू धर्म'],
            ['Buddhism', 'बौद्ध धर्म'],
            ['Sikhism', 'शीख धर्म'],
            ['Islam', 'इस्लाम धर्म'],
            ['Christianity', 'ख्रिश्चन धर्म']
        ]
    )

    language = models.StringField(
        label='आपण घरी कोणती भाषा बोलता?',
        choices=[
            ['Marathi', 'मराठी'],
            ['Hindi', 'हिंदी'],
            ['Telugu', 'तेेलगु'],
            ['Kannada', 'कन्नड'],
            ['Gujarati', 'गुजराती']
        ]
    )

    education = models.StringField(
        label='आपले शिक्षण स्तर काय आहे?',
        choices=[
            ['Primary (Std 1-5)', 'प्राथमिक (इयत्ता 1-5)'],
            ['Secondary (Std 8-12)', 'माध्यमिक (इयत्ता 8-12)'],
            ['Some college', 'काही महाविद्यालय'],
            ['College graduate and above', 'महाविद्यालयीन पदवी आणि त्यापेक्षा अधिक']
        ]
    )

    # family background
    totalFamilyMember = models.IntegerField(
        label='एकूण, आपल्या कुटुंबातील किती लोक?'
    )

    totalChildren = models.IntegerField(
        label='किती मुले आहेत?'
    )

    occupation = models.IntegerField(
        label='काय काम करतात?'
    )

    totalWorkingPeople = models.IntegerField(
        label='आज किती लोक कामावर गेले?'
    )

    preLockdownWorkingPeople = models.IntegerField(
        label='Lockdown करण्यापूर्वी किती लोक कामावर जात होते?'
    )

    totalIncome = models.IntegerField(
        label='Lockdown करण्यापूर्वी कुटुंबातील एकूण उत्पन्न किती होते?'
    )

    # Expenditure
    groceriesExpend = models.IntegerField(
        label='आपण आठवड्यात किराणा सामानावर किती खर्च करता?'
    )

    isOwnHouse = models.BooleanField(
        label='तुमचे स्वत: चे घर आहे का?',
        widget=widgets.RadioSelect,
        choices=yesNoChoice
    )

    MonthlyRent = models.IntegerField(
        label='आपण दरमहा किती भाडे द्याल?',
        blank=True
    )

    lastThreeMonthRent = models.BooleanField(
        label='आपण मागील तीन महिन्यांत पूर्ण भाडे रक्कम भरण्यास सक्षम आहात काय?',
        widget=widgets.RadioSelect,
        choices=yesNoChoice,
        blank=True
    )

    percentRentPaid = models.IntegerField(
        label='आपण भाड्याने किती टक्के दिले हे निर्दिष्ट करा.'
    )

    electricityExpense = models.IntegerField(
        label='आपण दरमहा विजेवर किती खर्च करता?'
    )

    LPGExpenses = models.IntegerField(
        label='आपण दरमहा गॅसवर किती खर्च करता?'
    )

    mobileExpense = models.IntegerField(
        label='आपण दरमहा मोबाइलवर किती खर्च करता?'
    )

    medicineExpense = models.IntegerField(
        label='दरमहा तुम्ही औषधांवर किती खर्च करता?'
    )

    isEmergencyExpense = models.BooleanField(
        label='गेल्या सहा महिन्यांत तुमच्यासाठी काही अनपेक्षित खर्च झाले - आरोग्यासाठी, भाड्याने देण्यासाठी, '
              'दुरुस्तीच्या कामासाठी, अन्नासाठी ...?',
        widget=widgets.RadioSelect,
        choices=yesNoChoice
    )

    EmergencyExpense = models.IntegerField(
        label='जर होय, तर किती रक्कम होती?'
    )

    heardRefinance = models.BooleanField(
        label='आपण पुनर्वित्त ऐकले आहे? मराठी मध्ये पुनर्निर्देशित. वित्तपुरवठा',
        widget=widgets.RadioSelect,
        choices=yesNoChoice
    )

    isRefinance = models.BooleanField(
        label='आपण कधीही पुनर्वित्त दिले आहे?',
        widget=widgets.RadioSelect,
        choices=yesNoChoice
    )

    refinaceAmt = models.IntegerField(
        label='पुनर्वित्त रक्कम आणि टक्केवारी किती होती?'
    )

    # Saving and Investment
    regularMonthlySavings = models.IntegerField(
        label='सामान्य परिस्थितीत, आपण दरमहा किती बचत कराल?'
    )

    lastSixMonthSavingUsed = models.IntegerField(
        label='मागील 6 महिन्यांत आपण किती बचत वापरली आहे?'
    )

    remainingSaving = models.IntegerField(
        label='आत्ता आपण किती बचत शिल्लक आहे?'
    )

    currentMonthlySavings = models.StringField(
        label='तुमच्या सध्याच्या उत्पन्नातून तुम्ही  किती बचत करीत आहात (रुपये मध्ये)?',
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ['Home', 'घरी'],
            ['Bank', 'एका बँकेत'],
            ['Other', 'इतर:']
        ]
    )

    bankSaving = models.IntegerField(
        label='तुम्ही बँकेत किती बचत करता?',
        blank=True
    )

    homeSaving = models.IntegerField(
        label='आपण घरी किती बचत कराल?',
        blank=True
    )

