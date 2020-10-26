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
    name_in_url = 'hybrid_hindi'
    players_per_group = None
    num_rounds = 1


yesNoChoice = [
    [True, 'हाँ'],
    [False, 'नही'],
]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    howmanypeople = models.IntegerField(label="आपके परिवार में कितने लोग हैं?",
                                        min=1,
                                        max=10,
                                        )
    howmanydependent = models.IntegerField(label="आर्थिक रूप से कितने निर्भर (बच्चों सहित)?",
                                           min=1,
                                           max=10,
                                           )
    wenttoworktoday = models.IntegerField(label="आज आपके घर में कितने लोग काम करने गए हैं?",
                                          min=1,
                                          max=10,
                                          )
    tempwork = models.BooleanField(
        label="क्या आपके परिवार का कोई सदस्य वर्तमान में अस्थायी या अंशकालिक काम कर रहा है?",
        choices=yesNoChoice)
    wenttoworkbeforelockdown = models.IntegerField(label="लॉकडाउन से पहले कितने लोग आपके घर में काम करने जा रहे थे?",
                                                   min=1,
                                                   max=10,
                                                   )
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
            [6, "अभी भी व्यवसाय या नौकरी है"],
            [7, "कभी कोई व्यवसाय या नौकरी नहीं थी"]])

    directlylostjob = models.IntegerField(
        label="क्या आपने अपनी नौकरी सीधे खो दी या आपको पहले आधा वेतन मिला, फिर अंत में छोड़ दिया?",
        choices=[
            [1, "सीधे नौकरी खो दी"],
            [2, "पहले मुझे आधा वेतन मिला, फिर मैंने अपनी नौकरी खो दी"],
            [3, "अभी भी एक व्यवसाय या नौकरी है"],
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
    jobsecureorfinding = models.IntegerField(
        label="क्या आपको लगता है कि आपकी नौकरी सुरक्षित है या आपको अगले तीन महीनों में नौकरी मिल जाएगी?",
        choices=yesNoChoice)
    lesssalary = models.IntegerField(
        label="क्या आपको लगता है कि अगर आपको नौकरी मिलती है, तो अगले तीन महीनों में आपको मिलने वाला वेतन पहले से कम हो जाएगा?",
        choices=yesNoChoice)
    losejob3months = models.IntegerField(
        label="यदि आप तीन महीने में एक व्यवसाय या नौकरी खो देते हैं, या अगले तीन महीनों में व्यवसाय या नौकरी नहीं पाते हैं, तो आप अपने परिवार का समर्थन कैसे करेंगे?",
        choices=[
            [1, "बचाए गए पैसों का इस्तेमाल करूंगा"],
            [2, "मैं निवेश की गई राशि का उपयोग करूंगा"],
            [3, "मैं उधार लूंगा"],
            [4, "मैं घर में कुछ बेचूंगा (सोना, चांदी ..)"],
            [5, "मैं अपने गाँव लौट जाऊंगा"],
        ])

    current_conditions = models.BooleanField(
        label="यदि वर्तमान स्थिति इस तरह जारी रहे, तो क्या आपको लगता है कि आप किराने का सामान, बिजली और मोबाइल के लिए पैसे देना जारी रख सकते हैं?",
        choices=yesNoChoice)
    howmuchpercentsavingsspent = models.IntegerField(
        label="लॉकडाउन के दौरान आपके द्वारा बचाए गए धन का कितना प्रतिशत खर्च किया गया था?",
        choices=[
            [1, "0-25%"],
            [2, "26-50%"],
            [3, "51-75%"],
            [4, "76-85%"],
            [5, "85-95%"],
            [6, "95-100%"]
        ])
    howmuchleftsavings = models.IntegerField(label="अब आपके पास (रुपयों में) कितनी बचत है?", choices=[
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
    doyouthinkthatisenough = models.BooleanField(
        label="यदि लॉकडाउन लंबे समय तक रहता है, तो क्या आपको लगता है कि उतनी बचत बस है?",
        choices=yesNoChoice)
    otherskill = models.IntegerField(label="क्या आपके पास एक अलग नौकरी खोजने के लिए एक और कौशल है?",
                                     choices=yesNoChoice)
    whatotherjob = models.IntegerField(label="आप किस और नौकरी की तलाश करेंगे?",
                                       choices=[
                                           [1, "निर्माण कार्य"],
                                           [2, "चपरासी की नौकरी"],
                                           [3, "डिलिव्हरी"],
                                           [4, "कृषि का काम"],
                                           [5, "दैनिक काम"],
                                           [6, "लिपिक कार्य"],
                                           [7, "अन्य"]
                                       ])
    willyougetone = models.BooleanField(label="क्या आपको लगता है कि आपको दूसरी नौकरी मिल सकती है?", choices=yesNoChoice)
    otherjobsalary = models.IntegerField(label="आपको क्या लगता है कि वेतन अन्य नौकरियों में है?", choices=[
        [1, "जितना मुझे अभी मिलता है"],
        [2, "अब मुझे जो मिलता है, उससे कम"],
        [3, "अब मुझसे ज्यादा मिलता है"]
    ])
    standardofliving = models.BooleanField(
        label="आपल्याला असे वाटते की एक विशिष्ट जीवनमान टिकवून ठेवण्यासाठी तो पगार समाधानकारक असेल?",
        choices=yesNoChoice)
    celebratediwali = models.BooleanField(label="क्या आपको लगता है कि आप इस साल दिवाली, ईद या क्रिसमस मनाएंगे?",
                                          choices=yesNoChoice)
    howmuchcanyouspend = models.IntegerField(label="आपको क्या लगता है कि आप कितना खर्च कर सकते हैं?", choices=[
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
    emergency10000rupees = models.IntegerField(
        label="यदि आपको तत्काल 10,000 रुपये की आवश्यकता है, उदाहरण के लिए अस्पताल में भर्ती के लिए, तो आप इसे कहां पा सकते हैं",
        choices=[
            [1, "मेरे पास है"],
            [2, "परिवार से पूछ के"],
            [3, "पड़ोसियों या रिश्तेदारों से पूछ के"],
            [4, "ऋणदाता से"],
            [5, "नहीं मिलेगा"],
        ])
    emergency50000rupees = models.IntegerField(
        label="यदि आपको तत्काल 50,000 रुपये की आवश्यकता है, उदाहरण के लिए अस्पताल में कई दिन बिताने के लिए, तो आपको यह कहां मिलेगा?",
        choices=[
            [1, "मेरे पास है"],
            [2, "परिवार से पूछ के"],
            [3, "पड़ोसियों या रिश्तेदारों से पूछ के"],
            [4, "ऋणदाता से"],
            [5, "नहीं मिलेगा"],
        ])
    emergency100000rupees = models.IntegerField(
        label="यदि आपको तत्काल 1,00,000 रुपये की आवश्यकता है, उदाहरण के लिए, यदि आपके पास दुर्घटना के बाद सर्जरी होनी है, तो आप इसे कहाँ प्राप्त करेंगे?",
        choices=[
            [1, "मेरे पास है"],
            [2, "परिवार से पूछ के"],
            [3, "पड़ोसियों या रिश्तेदारों से पूछ के"],
            [4, "ऋणदाता से"],
            [5, "नहीं मिलेगा"],
        ])

    emergency500000rupees = models.IntegerField(
        label="यदि आपको तत्काल 5,00,000 रुपये की आवश्यकता है, उदाहरण के लिए, यदि आपको किसी दुर्घटना के बाद बहुत गंभीर सर्जरी से गुजरना पड़ता है, तो आप इसे कहां पाएंगे?",
        choices=[
            [1, "मेरे पास है"],
            [2, "परिवार से पूछ के"],
            [3, "पड़ोसियों या रिश्तेदारों से पूछ के"],
            [4, "ऋणदाता से"],
            [5, "नहीं मिलेगा"],
        ])
    optimistic = models.IntegerField(label="0-3 में रेट करें कि आप अपने भविष्य को लेकर कितने आशावादी हैं", choices=[
        [1, "0"],
        [2, "1"],
        [3, "2"],
        [4, "3"]
    ])
