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
    name_in_url = 'incomeuncertainty_marathi'
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
    howmanypeople = models.IntegerField(label="आपल्या कुटुंबातील किती लोक आहेत?",
                                        min=1,
                                        max=10,
                                        )
    howmanydependent = models.IntegerField(label="किती आर्थिकदृष्ट्या अवलंबून (मुलांसह)?",
                                           min=1,
                                           max=10,
                                           )
    areyouemployed = models.IntegerField(label="तुम्ही सध्या व्यवसाय किंवा नोकरी करत आहात का?",
                                         choices=yesNoChoice)
    howmanymonthsago = models.IntegerField(
        label="जर व्यवसाय किंवा नोकरी नाही, तर, किती महिन्यांपूर्वी आपण व्यवसाय किंवा नोकरी गमावली?",
        choices=[
            [1, "1-3"],
            [2, "4-6"],
            [3, "7-9"],
            [4, "9-12"],
            [5, "12+"],
            [6, "अजूनही व्यवसाय किंवा नोकरी आहे"],
            [7, "व्यवसाय किंवा नोकरी कधीच नव्हती"]]
    )
    fullorpartial = models.IntegerField(
        label="आपला व्यवसाय किंवा नोकरी अस्ल्यास, आपण पूर्ण उत्पन्न किंवा पगार का आंशिक पगार घेत आहात?",
        choices=[
            [1, "पूर्ण उत्पन्न किंवा पगार"],
            [2, "आंशिक उत्पन्न किंवा पगार"],
            [3, "व्यवसाय किंवा नोकरी नाही आहे"],
            [4, "व्यवसाय किंवा नोकरी कधीच नव्हती"]]
    )
    groceries_weekly = models.IntegerField(label="आपण किराण्याच्या सामानावर दर आठवडा किती खर्च करता?", choices=[
        [1, "200-500"],
        [2, "501-1000"],
        [3, "1001-1500"],
        [4, "1501-2000"],
        [5, "2001 आणि अधिक"]
    ])
    groceries_gonedown = models.IntegerField(label="आपल्याला लोकडाऊनच्या आधी इतकं किराणा सामान आज कल परवडतं का?",
                                             choices=yesNoChoice)

    electricity_monthly = models.IntegerField(label="आपण दर महिना विजेवर किती खर्च करता?", choices=[
    [1, "200-500"],
    [2, "501-1000"],
    [3, "1001-1500"],
    [4, "1501-2000"],
    [5, "2001-2500"],
    [6, "2501-5000"],
    [7, "5001 आणि अधिक"]])

    electricity_goneup = models.IntegerField(label="मागील तीन महिन्यांत विजेवरचा खर्च वाढला आहे?", choices=yesNoChoice)
    mobile_monthly = models.IntegerField(label="आपण दरमहा मोबाइलवर किती खर्च करता?", choices=[
    [1, "200-500"],
    [2, "501-1000"],
    [3, "1001-1500"],
    [4, "1501-2000"],
    [5, "2001 आणि अधिक"]])
    mobile_goneup = models.IntegerField(label="मागील तीन महिन्यांत मोबाईलवरचा खर्च वाढला आहे?", choices=yesNoChoice)
    current_conditions = models.IntegerField(
    label="जर सध्याची आर्थिक परिस्थिती अशीच चालू राहिली तर, आपण किराणा सामान, वीज आणि मोबाइलसाठी पैसे देणे चालू ठेवू शकता असे आपल्याला वाटते का?",
    choices=yesNoChoice)

    unexpected_increase = models.IntegerField(label="मागील सहा महिन्यांत इतर कोणते खर्च अनपेक्षितपणे वाढले आहेत?", choices=[
    [1, "मुलांच्या शिक्षणावरचा खर्च"],
    [2, "औषदांवरचा किंवा हॉस्पिटलचा किंवा टेस्टिंगवरचा किंवा क्वारंटाईन वरचा खर्च"],
    [3, "प्रवासावरचा खर्च"],
    [4, "इतर"],
    [5, "अनपेक्षित खर्च आला नाही"]
])
    savingsbeforelockdown = models.IntegerField(label="लॉकडाउनपूर्वी आपण दर महिना किती बचत करायचा?", choices=[
    [1, "200-500"],
    [2, "501-1000"],
    [3, "1001-1500"],
    [4, "1501-2000"],
    [5, "2001-2500"],
    [6, "2501-5000"],
    [7, "5001-8000"],
    [8, "8001-10000"],
    [9, "10001 आणि अधिक"]
])
    howmuchpercentsavingsspent = models.IntegerField(label="बचत केलेले किती टक्के पैसे आपण लोकडाऊन च्या काळात खर्च केले?",
                                                 choices=[
                                                     [1, "0-25%"],
                                                     [2, "26-50%"],
                                                     [3, "51-75%"],
                                                     [4, "76-85%"],
                                                     [5, "85-95%"],
                                                     [6, "95-100%"]
                                                 ])
    howmuchleftsavings = models.IntegerField(label="आत्ता (रुपयांमध्ये) आपली किती बचत उरली आहे?", choices=[
    [1, "200-500"],
    [2, "501-1000"],
    [3, "1001-1500"],
    [4, "1501-2000"],
    [5, "2001-2500"],
    [6, "2501-5000"],
    [7, "5001-8000"],
    [8, "8001-10000"],
    [9, "10001 आणि अधिक"]
])
    doyouthinkthatisenough = models.IntegerField(
    label="जर लॉकडाउन अधिक काळ चालला तर आपल्याला वाटतं का कि ती रक्कम पुरेशी आहे?",
    choices=yesNoChoice)
    celebratediwali = models.IntegerField(label="आपणास असे वाटते की आपण यावर्षी दिवाळी, ईद किंवा क्रिसमस साजरा कराल?",
                                      choices=yesNoChoice)

    whatwillyouspendon = models.IntegerField(label="कशावर खर्च करू शकाल?", widget=widgets.checkbox, choices=[
    [1, "खाद्य पदार्थ"],
    [2, "मुलांसाठी कपडे"],
    [3, "सगळ्यांसाठी कपडे"],
    [4, "सोनं, चांदी, इ"]
])

    howmuchcanyouspend = models.IntegerField(label="अंदाजे आपण किती खर्च करू शकता असे वाटते?", choices=[
    [1, "200-500"],
    [2, "501-1000"],
    [3, "1001-1500"],
    [4, "1501-2000"],
    [5, "2001-2500"],
    [6, "2501-5000"],
    [7, "5001-8000"],
    [8, "8001-10000"],
    [9, "10001 आणि अधिक"]
])
    enoughfoodfortwomeals = models.IntegerField(
    label="सध्या घरात असलेल्या प्रत्येकासाठी दोनदा जेवणासाठी पुरेसे भोजन आहे का?", choices=yesNoChoice)
    howlongcanyouensurefood = models.IntegerField(
    label="लॉकडाउन अधिक काळ चालला तर आपल्याला वाटते का कि आपल्या कुटुंबाला २ वेळचं जेवण मिळत राहील?",
    choices=yesNoChoice)
    emergency1000rupees = models.IntegerField(
    label="आपल्याला त्वरित 1000 रुपयांची आवश्यकता असल्यास, उदाहरणार्थ डॉक्टरांच्या भेटीसाठी, आपल्याला ते कुठे ममिळतील?",
    choices=[
        [1, "माझ्याकडे आहेत"],
        [2, "घरातल्यांना विचारून"],
        [3, "शेजार-पाजाऱ्यांना किंवा नातेवाइकांना विचारून"],
        [4, "सावकाराकडून"],
        [5, "नाही मिळणार"],
    ])
    emergency10000rupees = models.IntegerField(
    label="आपल्याला त्वरित 10,000 रुपयांची आवश्यकता असल्यास, उदाहरणार्थ रुग्णालयात दाखल करण्यासाठी, आपल्याला ते कुठे ममिळतील?",
    choices=[
        [1, "माझ्याकडे आहेत"],
        [2, "घरातल्यांना विचारून"],
        [3, "शेजार-पाजाऱ्यांना किंवा नातेवाइकांना विचारून"],
        [4, "सावकाराकडून"],
        [5, "बँकेतून लोन घेऊन"],
        [6, "नाही मिळणार"],
    ])
    emergency50000rupees = models.IntegerField(
    label="आपल्याला त्वरित 50,000 रुपयांची आवश्यकता असल्यास, उदाहरणार्थ रूग्णालयात बरेच दिवस काढण्यासाठी, आपल्याला ते कुठे ममिळतील?",
    choices=[
        [1, "माझ्याकडे आहेत"],
        [2, "घरातल्यांना विचारून"],
        [3, "शेजार-पाजाऱ्यांना किंवा नातेवाइकांना विचारून"],
        [4, "सावकाराकडून"],
        [5, "बँकेतून लोन घेऊन"],
        [6, "नाही मिळणार"],
    ])
    emergency100000rupees = models.IntegerField(
    label="आपल्याला त्वरित 1,00,000 रुपयांची आवश्यकता असल्यास, उदाहरणार्थ अपघातानंतर शस्त्रक्रिया करावी लागल्यास, आपल्याला ते कुठे ममिळतील?",
    choices=[
        [1, "माझ्याकडे आहेत"],
        [2, "घरातल्यांना विचारून"],
        [3, "शेजार-पाजाऱ्यांना किंवा नातेवाइकांना विचारून"],
        [4, "सावकाराकडून"],
        [5, "बँकेतून लोन घेऊन"],
        [6, "नाही मिळणार"],
    ])

    emergency500000rupees = models.IntegerField(
    label="आपल्याला त्वरित 1,00,000 रुपयांची आवश्यकता असल्यास, उदाहरणार्थ अपघातानंतर खूप गंभीर शस्त्रक्रिया करावी लागल्यास, आपल्याला ते कुठे ममिळतील?",
    choices=[
        [1, "माझ्याकडे आहेत"],
        [2, "घरातल्यांना विचारून"],
        [3, "शेजार-पाजाऱ्यांना किंवा नातेवाइकांना विचारून"],
        [4, "सावकाराकडून"],
        [5, "बँकेतून लोन घेऊन"],
        [6, "नाही मिळणार"],
    ])
    optimistic = models.IntegerField(label="0-3 च्या प्रमाणात, आपण आपल्या भविष्याबद्दल किती आशावादी आहात?", choices=[
    [1, "0"],
    [2, "1"],
    [3, "2"],
    [4, "3"]
])
