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


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'hybrid_marathi'
    players_per_group = None
    num_rounds = 1

yesNoChoice = [
    [True, 'होय'],
    [False, 'नाही'],
]
class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    howmanypeople = models.IntegerField(label="आपल्या कुटुंबातील किती लोक आहेत?",
                                        min=1,
                                        max=10,
                                        )
    howmanydependent = models.IntegerField(label="किती आर्थिकदृष्ट्या अवलंबून (मुलांसह)?",
                                           min=1,
                                           max=10,
                                           )
    wenttoworktoday = models.IntegerField(label="आज तुमच्या घरात किती लोक कामावर गेले आहेत?",
                                          min=1,
                                          max=10,
                                          )
    tempwork = models.BooleanField(
        label="तुमच्या कुटुंबातील कोणतेही सदस्य सध्या तात्पुरते किंवा हंगामी नोकरी करतात का?",
        choices=yesNoChoice)
    wenttoworkbeforelockdown = models.IntegerField(label="लॉकडाउनपूर्वी तुमच्या घरात किती लोक कामावर जायचे?",
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
            [7, "व्यवसाय किंवा नोकरी कधीच नव्हती"]])

    directlylostjob = models.IntegerField(
        label="तुम्ही तुमची नोकरी थेट गमावली की तुम्हाला आधी निम्मा पगार मिळाला, मग शेवटी सोडण्यात आले?",
        choices=[
            [1, "थेट गमावली"],
            [2, "आधी मला अर्धा पगार मिळाला, मग नोकरी गमावली"],
            [3, "अजूनही व्यवसाय किंवा नोकरी आहे"],
            [4, "व्यवसाय किंवा नोकरी कधीच नव्हती"]
        ])
    fullorpartial = models.IntegerField(
        label="आपला व्यवसाय किंवा नोकरी अस्ल्यास, आपण पूर्ण उत्पन्न किंवा पगार का आंशिक पगार घेत आहात?",
        choices=[
            [1, "पूर्ण उत्पन्न किंवा पगार"],
            [2, "आंशिक उत्पन्न किंवा पगार"],
            [3, "व्यवसाय किंवा नोकरी नाही आहे"],
            [4, "व्यवसाय किंवा नोकरी कधीच नव्हती"]])
    jobsecureorfinding = models.IntegerField(label="तुम्हाला वाटते की तुमची नोकरी सुरक्षित आहे किंवा पुढील तीन "
                                                   "महिन्यांत तुम्हाला नोकरी मिळेल?",
                                             choices=[[1, "हो"], [2, "नाही"], [3,
                                                                               "कदाचित"]])
    lesssalary = models.IntegerField(label="आपल्याला असे वाटते का कि, जर नोकरी मिळाली, तर जो पगार पुढील तीन महिन्यात "
                                           "मिळेल तो पूर्वीपेक्षा कमी मिळेल?",
                                     choices=[[1, "हो"], [2, "नाही"], [3, "कदाचित"]])
    losejob3months = models.IntegerField(label="जर आपण तीन महिन्यात व्यवसाय किंवा नोकरी गमावल्यास, किंवा पुढील तीन "
                                               "महिन्यांत व्यवसाय किंवा नोकरी न मिळाल्यास, आपण आपल्या कुटुंबाची कशी "
                                               "पूर्तता कराल?",
                                         choices=[
                                             [1, "बचत केलेले पैसे मी वापरेन"],
                                             [2, "गुंतवलेली रक्कम मी वापरेन"],
                                             [3, "मी कर्ज घेईन"],
                                             [4, "मी घरातील काहीतरी विकेन (सोने, चांदी..)"],
                                             [5, "मी माझ्या गावी परत जाईन"],
                                         ])

    current_conditions = models.IntegerField(
        label="जर सध्याची आर्थिक परिस्थिती अशीच चालू राहिली तर, आपण किराणा सामान, वीज आणि मोबाइलसाठी पैसे देणे चालू ठेवू शकता असे आपल्याला वाटते का?",
        choices=yesNoChoice)
    howmuchpercentsavingsspent = models.IntegerField(
        label="बचत केलेले किती टक्के पैसे आपण लोकडाऊन च्या काळात खर्च केले?",
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
    otherskill = models.IntegerField(label="आपल्याकडे वेगळी नोकरी शोधण्यासाठी आणखी एक कौशल्य आहे?", choices=yesNoChoice)
    whatotherjob = models.IntegerField(label="आपण कोणती दुसरी नोकरी शोधाल?",
                                       choices=[
                                           [1, "बांधकाम चे काम"],
                                           [2, "शिपाई ची नोकरी"],
                                           [3, "डिलिव्हरी"],
                                           [4, "शेतीचे काम"],
                                           [5, "रोजंदारीचे काम"],
                                           [6, "कारकुनी काम"],
                                           [7, "इतर"]
                                       ])
    willyougetone = models.BooleanField(label="तुम्हाला वाटते की तुम्हाला दुसरी नोकरी मिळेल?", choices=yesNoChoice)
    otherjobsalary = models.IntegerField(label="इतर नोकरीत पगार म्हणजे काय असे तुम्हाला वाटते?", choices=[
        [1, "मी आता जितके मिळवितो तितकेच"],
        [2, "मी आता जे मिळवितो त्यापेक्षा कमी"],
        [3, "मी आता मिळवण्यापेक्षा अधिक"]
    ])
    standardofliving = models.BooleanField(
        label="आपल्याला असे वाटते की एक विशिष्ट जीवनमान टिकवून ठेवण्यासाठी तो पगार समाधानकारक असेल?",
        choices=yesNoChoice)
    celebratediwali = models.IntegerField(label="आपणास असे वाटते की आपण यावर्षी दिवाळी, ईद किंवा क्रिसमस साजरा कराल?",
                                          choices=yesNoChoice)
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

