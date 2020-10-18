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
    howmanypeople=models.IntegerField(label="आपल्या कुटुंबातील किती लोक आहेत?",
                                      min=1,
                                      max=10,
                                      )
    howmanydependent=models.IntegerField(label="किती आर्थिकदृष्ट्या अवलंबून (मुलांसह)?",
                                         min=1,
                                         max=10,
                                         )
    wenttoworktoday=models.IntegerField(label="आज तुमच्या घरात किती लोक कामावर गेले आहेत?",
                                        min=1,
                                        max=10,
                                        )
    wenttoworkbeforelockdown=models.IntegerField(label="लॉकडाउनपूर्वी तुमच्या घरात किती लोक कामावर जायचे?",
                                                 min=1,
                                                 max=10,
                                                 )
    tempwork = models.IntegerField(label="तुमच्या कुटुंबातील कोणतेही सदस्य सध्या तात्पुरते किंवा हंगामी नोकरी करतात का?",
                                   choices=yesNoChoice)
    areyouemployed=models.IntegerField(label="तुम्ही सध्या व्यवसाय किंवा नोकरी करत आहात का?",
                                       choices=yesNoChoice)
    howmanymonthsago=models.IntegerField(label="जर व्यवसाय किंवा नोकरी नाही, तर, किती महिन्यांपूर्वी आपण व्यवसाय किंवा नोकरी गमावली?",
                                         choices=[
                                             [1,"1-3"],
                                             [2,"4-6"],
                                             [3,"7-9"],
                                             [4,"9-12"],
                                             [5,"12+"],
                                             [6, "अजूनही व्यवसाय किंवा नोकरी आहे"],
                                             [7, "व्यवसाय किंवा नोकरी कधीच नव्हती"]
                                         ])
    directlylostjob=models.IntegerField(label="तुम्ही तुमची नोकरी थेट गमावली की तुम्हाला आधी निम्मा पगार मिळाला, मग शेवटी सोडण्यात आले?",
                                        choices=[
                                            [1,"थेट गमावली"],
                                            [2,"आधी मला अर्धा पगार मिळाला, मग नोकरी गमावली"],
                                            [3,"अजूनही व्यवसाय किंवा नोकरी आहे"],
                                            [4,"व्यवसाय किंवा नोकरी कधीच नव्हती"]
                                        ])
    fullorpartial=models.IntegerField(label="आपला व्यवसाय किंवा नोकरी अस्ल्यास, आपण पूर्ण उत्पन्न किंवा पगार का आंशिक पगार घेत आहात?",
                                      choices=[
                                          [1,"पूर्ण उत्पन्न किंवा पगार"],
                                          [2,"आंशिक उत्पन्न किंवा पगार"],
                                          [3, "व्यवसाय किंवा नोकरी नाही आहे"],
                                          [4,"व्यवसाय किंवा नोकरी कधीच नव्हती"]
                                      ])
    ifpartial=models.IntegerField(label="आंशिक असल्यास, आपण किती उत्पन्न किंवा पगार प्राप्त करीत आहात?",
                                  choices=[
                                      [1,"अर्ध्यापेक्षा जास्त"],
                                      [2,"अर्धा"],
                                      [3, "अर्ध्यापेक्षा कमी"],
                                      [4, "पूर्ण उत्पन्न किंवा पगार मिळत आहे"],
                                      [5, "व्यवसाय किंवा नोकरी नाही आहे"],
                                      [6, "व्यवसाय किंवा नोकरी कधीच नव्हती"]
                                  ])
    otheremployed=models.IntegerField(label="सध्या कुटूंबातील इतर एखादा सदस्य व्यवसाय किंवा नोकरी करतो का?",
                                      choices=yesNoChoice)
    otherfullorpartial=models.IntegerField(label="जर हो, तर त्यांना पूर्ण उत्पन्न किंवा पगार मिळतो की अंशतः?",
                                           choices=[
                                          [1,"पूर्ण उत्पन्न किंवा पगार"],
                                          [2,"आंशिक उत्पन्न किंवा पगार"],
                                          [3, "व्यवसाय किंवा नोकरी नाही आहे"],
                                          [4,"व्यवसाय किंवा नोकरी कधीच नव्हती"]
                                      ]))
    otherifpartial=models.IntegerField(label="आंशिक असल्यास, ते किती प्राप्त करीत आहेत?",
                                  choices=[
                                      [1,"अर्ध्यापेक्षा जास्त"],
                                      [2,"अर्धा"],
                                      [3, "अर्ध्यापेक्षा कमी"],
                                      [4, "पूर्ण उत्पन्न किंवा पगार मिळत आहे"],
                                      [5, "व्यवसाय किंवा नोकरी नाही आहे"],
                                      [6, "व्यवसाय किंवा नोकरी कधीच नव्हती"]
                                  ])
    incomebeforelockdown=models.IntegerField(label="लॉकडाउनअधी कुटुंबातील एकूण उत्पन्न किती होते?", choices=[
        [1,"5000 किंवा कमी"],
        [2,"5000 - 7500"],
        [3,"7500 - 10,000"],
        [4,"10,000 - 12,500"],
        [5,"12,500 - 15,000"],
        [6,"15,000 - 20,000"],
        [7,"20,000 - 25,000"],
        [8,"25,000 किंवा जास्त"]
    ])
    incometoday=models.IntegerField(label="आज कौटुंबिक उत्पन्न किती आहे?", choices=[
        [1,"5000 किंवा कमी"],
        [2,"5000 - 7500"],
        [3,"7500 - 10,000"],
        [4,"10,000 - 12,500"],
        [5,"12,500 - 15,000"],
        [6,"15,000 - 20,000"],
        [7,"20,000 - 25,000"],
        [8,"25,000 किंवा जास्त"]
    ])
    jobsecureorfinding=models.IntegerField(label="तुम्हाला वाटते की तुमची नोकरी सुरक्षित आहे किंवा पुढील तीन महिन्यांत तुम्हाला नोकरी मिळेल?",choices=[[1,"हो"],[2,"नाही"],[3,"कदाचित"]])
    lesssalary=models.IntegerField(label="आपल्याला असे वाटते का कि, जर नोकरी मिळाली, तर जो पगार पुढील तीन महिन्यात मिळेल तो पूर्वीपेक्षा कमी मिळेल?",choices=[[1,"हो"],[2,"नाही"],[3,"कदाचित"]])
    otherjobssecureorfinding=models.IntegerField(label="आपणास असे वाटते की आपल्या कुटुंबातील सदस्याची व्यवसाय किंवा नोकरी सुरक्षित आहे किंवा पुढील तीन महिन्यांत त्यांना व्यवसाय किंवा नोकरी मिळेल?",choices=[[1,"हो"],[2,"नाही"],[3,"कदाचित"]])
    otherlesssalary=models.IntegerField(label="तुम्हाला वाटत आहे की येत्या तीन महिन्यांत त्यांना मिळणार्या उत्पन्न किंवा पगारापेक्षा कमी पगार मिळेल?",choices=[[1,"हो"],[2,"नाही"],[3,"कदाचित"]])
    losejob3months=models.IntegerField(label="जर आपण तीन महिन्यात व्यवसाय किंवा नोकरी गमावल्यास, किंवा पुढील तीन महिन्यांत व्यवसाय किंवा नोकरी न मिळाल्यास, आपण आपल्या कुटुंबाची कशी पूर्तता कराल?",
    choices=[
        [1, "बचत केलेले पैसे मी वापरेन"],
        [2, "गुंतवलेली रक्कम मी वापरेन"],
        [3, "मी कर्ज घेईन"],
        [4, "मी घरातील काहीतरी विकेन (सोने, चांदी..)"],
        [5, "मी माझ्या गावी परत जाईन"],
    ])
    otherskill=models.IntegerField(label="आपल्याकडे वेगळी नोकरी शोधण्यासाठी आणखी एक कौशल्य आहे?", choices=yesNoChoice)
    whatotherjob=models.IntegerField(label="आपण कोणती दुसरी नोकरी शोधाल?",
choices=[
    [1,"बांधकाम चे काम"],
    [2, "शिपाई ची नोकरी"],
    [3, "डिलिव्हरी"],
    [4, "शेतीचे काम"],
    [5, "रोजंदारीचे काम"],
    [6, "कारकुनी काम"],
    [7, "इतर"]
])
    willyougetone=models.IntegerField(label="तुम्हाला वाटते की तुम्हाला दुसरी नोकरी मिळेल?",choices=yesNoChoice)
    otherjobsalary=models.IntegerField(label="इतर नोकरीत पगार म्हणजे काय असे तुम्हाला वाटते?", choices=[
        [1, "मी आता जितके मिळवितो तितकेच"],
        [2, "मी आता जे मिळवितो त्यापेक्षा कमी"],
        [3, "मी आता मिळवण्यापेक्षा अधिक"]
    ])
    standardofliving=models.IntegerField(label="आपल्याला असे वाटते की एक विशिष्ट जीवनमान टिकवून ठेवण्यासाठी तो पगार समाधानकारक असेल?",choices=yesNoChoice)
    twojobs=models.IntegerField(label="आपल्याला असे वाटते की जीवनमान टिकविण्यासाठी आपल्याला दोन नोकर्या घ्याव्या लागतील?",choices=yesNoChoice)
    competitiontofind=models.IntegerField(label="आपणास असे वाटते की दोन नोकर्‍या शोधण्यात आपल्यात खूप स्पर्धा आहे?", choices=yesNoChoice)
    physicallywell=models.IntegerField(label="आपल्याला असे वाटते की आपण दोन नोकरीसाठी शारीरिकदृष्ट्या चांगले आहात?", choices=yesNoChoice)
    covidhealth=models.IntegerField(label="आपण चिंता करतात का आपणास कोविड झाल्यास, आपल्या दीर्घकालीन आरोग्यावर परिणाम होईल आणि यामुळे कायमचे काम करण्याची शारीरिक क्षमतेवर परिणाम होईल?",choices=yesNoChoice)
    optimistic=models.IntegerField(label="0-3 च्या प्रमाणात, आपण आपल्या भविष्याबद्दल किती आशावादी आहात?",choices=[
        [1,"0"],
        [2, "1"],
        [3, "2"],
        [4, "3"]
    ])