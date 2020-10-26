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
    name_in_url = "SES_hindi"
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


yesNoChoice = [
    [True, 'हाँ'],
    [False, 'नही'],
]


class Player(BasePlayer):
    hungerRate = models.IntegerField(
        label='प्रयोग के दौरान आपको कितनी भूख लगी थी उसका रेटिंग दीजिये (1 ते 5)',
        min=1,
        max=5,
    )

    tiredRate = models.IntegerField(
        label='प्रयोग के दौरान आप कितने थके हुए थे उसका रेटिंग दीजिये (1 ते 5)',
        min=1,
        max=5,
    )

    age = models.IntegerField(
        label='आपकी उम्र क्या हैं?'
    )

    gender = models.StringField(
        label='आपका लिंग क्या है?',
        widget=widgets.RadioSelect,
        choices=[
            ['Male', 'पुरुष'],
            ['female', 'महिला']
        ],
    )

    isMarried = models.BooleanField(
        label='क्या आप शादीशुदा है?',
        widget=widgets.RadioSelect,
        choices=yesNoChoice
    )

    religion = models.StringField(
        label='आपका क्या धर्म है? ',
        choices=[
            ['Hinduism', 'हिंदू धर्म'],
            ['Buddhism', 'बौद्ध धर्म'],
            ['Sikhism', 'शीख धर्म'],
            ['Islam', 'इस्लाम धर्म'],
            ['Christianity', 'ख्रिश्चन धर्म']
        ]
    )

    language = models.StringField(
        label='आप घर पर कौन सी भाषा बोलते हैं?',
        choices=[
            ['Marathi', 'मराठी'],
            ['Hindi', 'हिंदी'],
            ['Telugu', 'तेेलगु'],
            ['Kannada', 'कन्नड'],
            ['Gujarati', 'गुजराती']
        ]
    )

    education = models.StringField(
        label='आप कहा तक पढ़े है?',
        choices=[
            ['Primary (Std 1-5)', 'प्राथमिक (इयत्ता 1-5)'],
            ['Secondary (Std 8-12)', 'माध्यमिक (इयत्ता 8-12)'],
            ['Some college', 'कुछ कॉलेज'],
            ['College graduate and above', 'कॉलेज की डिग्री और ऊपर']
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
        label='आप क्या करते हैं?', choices=[
            [1, "सरकारी नौकरी"],
            [2, "अपना व्यवसाय"],
            [3, "घर में व्यवसाय"],
            [4, "कारखाने के कर्मचारी"],
            [5, "रिक्शा या टैक्सी ड्राइवर या डिलीवरी का काम"],
            [6, "एक बड़ी कंपनी में नौकरी"],
            [7, "चिकित्सा क्षेत्र (वार्ड बॉय, नर्स आदि)"],
            [8, "शिक्षक"],
            [9, "इतर"],
            [10, "कभी नौकरी नहीं की थी"]
        ]
    )
    useofhands = models.BooleanField(
        label="क्या आपके हाथों का उपयोग आपके व्यवसाय का एक बड़ा हिस्सा है? (उदाहरण: कारखाना कर्मचारी, दर्जी ...)",
        widget=widgets.RadioSelect,
        choices=yesNoChoice
    )

    isOwnHouse = models.BooleanField(
        label='क्या आपका अपना घर है?',
        widget=widgets.RadioSelect,
        choices=yesNoChoice
    )

    hasbankaccount = models.BooleanField(label="क्या आपके पास बैंक खाता है?",
                                         widget=widgets.RadioSelect,
                                         choices=yesNoChoice)

    hasFD = models.BooleanField(label="क्या आपके पास फिक्स्ड डिपॉजिट (एफ डी) हैं?",
                                widget=widgets.RadioSelect,
                                choices=yesNoChoice)

    hasmutualfunds = models.BooleanField(label="क्या आपके पास म्यूचुअल फंड हैं?",
                                         widget=widgets.RadioSelect,
                                         choices=yesNoChoice)

    hasinsurance = models.BooleanField(label="क्या आपका बीमा है?",
                                       widget=widgets.RadioSelect,
                                       choices=yesNoChoice)
    gotcovid = models.BooleanField(label=" क्या आपको कोरोनावायरस हुआ था?",
                                   widget=widgets.RadioSelect,
                                   choices=yesNoChoice)
    notnenoughfood = models.BooleanField(
        label="क्या पिछले छह महीनों में ऐसा समय आया था जब आपके पास पर्याप्त (enough) भोजन नहीं था?",
        widget=widgets.RadioSelect,
        choices=yesNoChoice)
    howmanytimes = models.IntegerField(label="ऐसा कितनी बार हुआ?",
                                       choices=[
                                           [1, "1-2"],
                                           [2, "3-4"],
                                           [3, "5-6"],
                                           [4, "7-8"],
                                           [5, "8 और अधिक"],
                                           [6, "ऐसा कभी नहीं हुआ"]
                                       ])
