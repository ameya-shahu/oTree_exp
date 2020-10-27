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
    name_in_url = 'incomeuncertainty_hindi'
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

yesNoMaybeChoice = [
    [1, "हो"], [2, "नाही"], [3, "कदाचित"]
]


class Player(BasePlayer):
    howmanypeople = models.IntegerField(label="आपके परिवार में कितने लोग हैं?",
                                        min=0,
                                        max=10,
                                        )
    howmanydependent = models.IntegerField(label="आर्थिक रूप से कितने निर्भर (बच्चों सहित)?",
                                           min=0,
                                           max=10,
                                           )
    wenttoworktoday = models.IntegerField(label="आज आपके घर में कितने लोग काम करने गए हैं?",
                                          min=0,
                                          max=10,
                                          )
    wenttoworkbeforelockdown = models.IntegerField(label="लॉकडाउन से पहले कितने लोग आपके घर में काम करने जा रहे थे?",
                                                   min=0,
                                                   max=10,
                                                   )
    tempwork = models.BooleanField(
        label="क्या आपके परिवार का कोई सदस्य वर्तमान में अस्थायी या अंशकालिक (seasonal or temporary) काम कर रहा है?",
        choices=yesNoChoice)
    areyouemployed = models.BooleanField(label="क्या आप अभी व्यवसाय या नौकरी कर रहे हैं?",
                                         choices=yesNoChoice)
    howmanymonthsago = models.IntegerField(
        label="यदि कोई व्यवसाय या नौकरी नहीं है, तो आपने कितने महीने पहले अपना व्यवसाय या नौकरी खो दी थी?",
        choices=[
            [1, "1-3"],
            [2, "4-6"],
            [3, "7-9"],
            [4, "9-12"],
            [5, "12+"],
            [6, "अभी भी एक व्यवसाय या नौकरी है"],
            [7, "कभी कोई व्यवसाय या नौकरी नहीं थी"]
        ])
    directlylostjob = models.IntegerField(
        label="क्या आपने अपनी नौकरी सीधे खो दी या आपको पहले आधा वेतन मिला, फिर अंत में छोड़ दिया?",
        choices=[
            [1, "सीधे नौकरी खो दी"],
            [2, "पहले मुझे आधा वेतन मिला, फिर मैंने अपनी नौकरी खो दी"],
            [3, "अभी भी व्यवसाय या नौकरी है"],
            [4, "कभी कोई व्यवसाय या नौकरी नहीं थी"]
        ])
    fullorpartial = models.IntegerField(
        label="यदि आपके पास कोई व्यवसाय या नौकरी है, तो क्या आप पूरी आमदनी या वेतन या आंशिक वेतन ले रहे हैं?",
        choices=[
            [1, "पूरी आमदनी या वेतन"],
            [2, "आंशिक आय या वेतन"],
            [3, "कोई व्यवसाय या नौकरी नहीं हैे"],
            [4, "कभी कोई व्यवसाय या नौकरी नहीं थी"]
        ])
    ifpartial = models.IntegerField(label="यदि आंशिक है, तो आप कितनी आय या वेतन प्राप्त कर रहे हैं?",
                                    choices=[
                                        [1, "आधे से ज्यादा"],
                                        [2, "आधा"],
                                        [3, "आधे से कम"],
                                        [4, "पूरी आमदनी या वेतन"],
                                        [5, "कोई व्यवसाय या नौकरी नहीं हैे"],
                                        [6, "कभी कोई व्यवसाय या नौकरी नहीं थी"]
                                    ])
    otheremployed = models.BooleanField(
        label="क्या परिवार के किसी अन्य सदस्य के पास वर्तमान में कोई व्यवसाय या नौकरी है?",
        choices=yesNoChoice)
    otherfullorpartial = models.IntegerField(
        label="यदि हां, तो क्या उन्हें पूरी आय या वेतन या इसका कुछ हिस्सा मिलता है?",
        choices=[
            [1, "पूरी आमदनी या वेतन"],
            [2, "आंशिक आय या वेतन"],
            [3, "कोई व्यवसाय या नौकरी नहीं हैे"],
            [4, "कभी कोई व्यवसाय या नौकरी नहीं थी"]
        ])
    otherifpartial = models.IntegerField(label="यदि आंशिक है, तो वे कितना प्राप्त कर रहे हैं?",
                                         choices=[
                                             [1, "आधे से ज्यादा"],
                                             [2, "आधा"],
                                             [3, "आधे से कम"],
                                             [4, "पूरी आमदनी या वेतन"],
                                             [5, "कोई व्यवसाय या नौकरी नहीं हैे"],
                                             [6, "कभी कोई व्यवसाय या नौकरी नहीं थी"]
                                         ])
    incomebeforelockdown = models.IntegerField(label="लॉकडाउन से पहले परिवार की कुल आय क्या थी?", choices=[
        [1, "5000 या कम"],
        [2, "5000 - 7500"],
        [3, "7500 - 10,000"],
        [4, "10,000 - 12,500"],
        [5, "12,500 - 15,000"],
        [6, "15,000 - 20,000"],
        [7, "20,000 - 25,000"],
        [8, "25,000 या ज्यादा"]
    ])
    incometoday = models.IntegerField(label="आज पारिवारिक आय क्या है?", choices=[
        [1, "5000 या कम"],
        [2, "5000 - 7500"],
        [3, "7500 - 10,000"],
        [4, "10,000 - 12,500"],
        [5, "12,500 - 15,000"],
        [6, "15,000 - 20,000"],
        [7, "20,000 - 25,000"],
        [8, "25,000 या ज्यादा"]
    ])
    jobsecureorfinding = models.BooleanField(
        label="क्या आपको लगता है कि आपकी नौकरी सुरक्षित है या आपको अगले तीन महीनों में नौकरी मिल जाएगी?",
        choices=yesNoChoice)
    lesssalary = models.BooleanField(
        label="क्या आपको लगता है कि अगर आपको नौकरी मिलती है, तो अगले तीन महीनों में आपको मिलने वाला वेतन पहले से कम हो जाएगा?",
        choices=yesNoChoice)
    otherjobssecureorfinding = models.BooleanField(
        label="क्या आपको लगता है कि आपके परिवार के सदस्य का व्यवसाय या नौकरी सुरक्षित है या उन्हें अगले तीन महीनों में व्यवसाय या नौकरी मिल जाएगी?",
        choices=yesNoChoice)
    otherlesssalary = models.BooleanField(
        label="क्या आपको लगता है कि अगले तीन महीनों में उन्हें अपनी आय या वेतन से कम वेतन मिलेगा?",
        choices=yesNoChoice)
    losejob3months = models.IntegerField(
        label="यदि आप तीन महीने में एक व्यवसाय या नौकरी खो देते हैं, या अगले तीन महीनों में व्यवसाय या नौकरी नहीं पाते हैं, तो आप अपने परिवार का पोशन कैसे करेंगे?",
        choices=[
            [1, "बचाए गए पैसों का इस्तेमाल करूंगा"],
            [2, "मैं निवेश (invest) की गई रकम का उपयोग करूंगा"],
            [3, "मैं उधार लूंगा"],
            [4, "मैं घर में कुछ बेचूंगा (सोना, चांदी ..)"],
            [5, "मैं अपने गाँव लौट जाऊंगा"],
        ])
    otherskill = models.BooleanField(label="क्या आपके पास एक अलग नौकरी खोजने के लिए एक और कौशल है?",
                                     choices=yesNoChoice)
    whatotherjob = models.IntegerField(label="आप किस और नौकरी की तलाश करेंगे?",
                                       choices=[
                                           [1, "कन्स्त्रक्शन काम"],
                                           [2, "चपरासी की नौकरी"],
                                           [3, "डिलिव्हरी"],
                                           [4, "कृषि का काम"],
                                           [5, "दैनिक काम"],
                                           [6, "क्लर्क कार्य"],
                                           [7, "अन्य"]
                                       ])
    willyougetone = models.BooleanField(label="क्या आपको लगता है कि आपको दूसरी नौकरी मिल सकती है?", choices=yesNoChoice)
    otherjobsalary = models.IntegerField(label="आपको क्या लगता है कि वेतन अन्य नौकरियों में है?", choices=[
        [1, "जितना मुझे अभी मिलता है"],
        [2, "अब मुझे जो मिलता है, उससे कम"],
        [3, "अब मुझसे ज्यादा मिलता है"]
    ])
    standardofliving = models.BooleanField(
        label="क्या आपको लगता है कि एक निश्चित जीवन स्तर बनाए रखने के लिए वेतन संतोषजनक होगा?",
        choices=yesNoChoice)
    twojobs = models.BooleanField(
        label="क्या आपको लगता है कि जीवनमान टिकाने के लिए आपको दो काम करने होंगे?", choices=yesNoChoice)
    competitiontofind = models.BooleanField(
        label="क्या आपको लगता है कि दो नौकरियों को खोजने के लिए लोगो के बीच बहुत प्रतिस्पर्धा है?",
        choices=yesNoChoice)
    physicallywell = models.BooleanField(label="क्या आपको लगता है कि आप दो नौकरियों के लिए शारीरिक रूप से फिट हैं?",
                                         choices=yesNoChoice)
    covidhealth = models.BooleanField(
        label="क्या आप चिंतित हैं कि यदि आपको कोरोना्वाइरस होता है, तो यह आपके दीर्घकालिक स्वास्थ्य को प्रभावित करेगा और स्थायी रूप से काम करने की आपकी शारीरिक क्षमता को प्रभावित करेगा?",
        choices=yesNoChoice)
    optimistic = models.IntegerField(label="0-3 पर, आप अपने भविष्य को लेकर कितने आशावादी हैं?", choices=[0, 1, 2, 3])
