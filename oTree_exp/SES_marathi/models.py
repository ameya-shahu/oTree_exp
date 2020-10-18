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
        max=5,
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
    # totalFamilyMember = models.IntegerField(
    #     label='एकूण, आपल्या कुटुंबातील किती लोक?'
    # )
    #
    # totalChildren = models.IntegerField(
    #     label='किती मुले आहेत?'
    # )

    occupation = models.IntegerField(
        label='आपण काय काम करतात?', choices=[
            [1, "सरकारी नोकरी"],
            [2, "स्वत: चा व्यवसाय"],
            [3, "घरगुती व्यवसाय"],
            [4, "कारखान्यात कामगार"],
            [5, "रिक्षा किंवा टॅक्सी ड्रायव्हर किंवा डिलिव्हरी चे काम"],
            [6, "मोठ्या कंपनीत नोकरी"],
            [7, "वैद्यकीय क्षेत्र (वार्ड बोय, नर्स इ.)"],
            [8, "शिक्षक"],
            [9, "इतर"],
            [10, "नोकरी कधीच नव्हती"]
        ]
    )
    useofhands = models.BooleanField(
        label="आपल्या हाताचा वापर करणं हे आपल्या व्यवसायाचा खूप मोठा भाग आहे का? (उदाहरणार्थ: फॅक्टरी कामगार, टेलर ...)",
        widget=widgets.RadioSelect,
        choices=yesNoChoice
    )

    isOwnHouse = models.BooleanField(
        label='तुमचे स्वत: चे घर आहे का?',
        widget=widgets.RadioSelect,
        choices=yesNoChoice
    )

    hasbankaccount = models.BooleanField(label="आपला बँक अकाउंट आहे का ?",
                                         widget=widgets.RadioSelect,
                                         choices=yesNoChoice)

    hasFD = models.BooleanField(label="आपला बँक अकाउंट आहे का ?",
                                widget=widgets.RadioSelect,
                                choices=yesNoChoice)

    hasmutualfunds = models.BooleanField(label="आपला म्युच्युअल फंडस् आहे का ?",
                                         widget=widgets.RadioSelect,
                                         choices=yesNoChoice)

    hasinsurance = models.BooleanField(label="आपल्याकडे विमा आहे का?",
                                       widget=widgets.RadioSelect,
                                       choices=yesNoChoice)
    gotcovid = models.BooleanField(label="आपल्याला कोवीड  झाला होता का?",
                                   widget=widgets.RadioSelect,
                                   choices=yesNoChoice)
    notnenoughfood = models.BooleanField(
        label="गेल्या सहा महिन्यांत अशी वेळ आली आहे का जेव्हा तुमच्याकडे पुरेसे अन्न नव्हते?",
        widget=widgets.RadioSelect,
        choices=yesNoChoice)
    howmanytimes = models.IntegerField(label="किती वेळा असे घडले?",
                                       choices=[
                                           [1, "1-2"],
                                           [2, "3-4"],
                                           [3, "5-6"],
                                           [4, "7-8"],
                                           [5, "8 आणि अधिक"],
                                           [6, "कधीच असे घडले नाही"]
                                       ])
