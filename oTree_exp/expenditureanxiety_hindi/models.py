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
    name_in_url = "expenditureanxiety_hindi"
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
    howmanypeople = models.IntegerField(label="आपके परिवार में कितने लोग हैं?",
                                        min=1,
                                        max=10,
                                        )
    howmanydependent = models.IntegerField(label="आर्थिक रूप से कितने निर्भर (बच्चों सहित)?",
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
            [7, "कभी कोई व्यवसाय या नौकरी नहीं थी"]]
    )
    fullorpartial = models.IntegerField(
        label="यदि आपके पास कोई व्यवसाय या नौकरी है, तो आप पूरी या आंशिक वेतन (salary) ले रहे हैं?",
        choices=[
            [1, "पूरी आमदनी या वेतन"],
            [2, "आंशिक आमदनी या वेतन"],
            [3, "कोई व्यवसाय या नौकरी नहीं है"],
            [4, "कभी कोई व्यवसाय या नौकरी नहीं थी"]]
    )
    groceries_weekly = models.IntegerField(label="आप किराने का सामान पर प्रति सप्ताह कितना खर्च करते हैं?", choices=[
        [1, "200-500"],
        [2, "501-1000"],
        [3, "1001-1500"],
        [4, "1501-2000"],
        [5, "2001 और अधिक"]
    ])
    groceries_gonedown = models.BooleanField(label="लॉकडाउन से पहले आप जितने िराने का सामान खरीद सकते हैं, क्या आप उतने ही लॉकडाउन के बाद भी खरीद सकते हैं?",
                                             choices=yesNoChoice)

    electricity_monthly = models.IntegerField(label="आप प्रति माह बिजली पर कितना खर्च करते हैं?", choices=[
    [1, "200-500"],
    [2, "501-1000"],
    [3, "1001-1500"],
    [4, "1501-2000"],
    [5, "2001-2500"],
    [6, "2501-5000"],
    [7, "5001 और अधिक"]])

    electricity_goneup = models.BooleanField(label="क्या पिछले तीन महीनों में बिजली का बिल बढ़ी है?", choices=yesNoChoice)
    mobile_monthly = models.IntegerField(label="आप हर महीने मोबाइल पर कितना खर्च करते हैं?", choices=[
    [1, "200-500"],
    [2, "501-1000"],
    [3, "1001-1500"],
    [4, "1501-2000"],
    [5, "2001 और अधिक"]])
    mobile_goneup = models.BooleanField(label="क्या पिछले तीन महीनों में मोबाइल का खर्च बढ़ा है?", choices=yesNoChoice)
    current_conditions = models.BooleanField(
    label="यदि वर्तमान स्थिति इस तरह जारी रहे, तो क्या आपको लगता है कि आप किराने का सामान, बिजली और मोबाइल के लिए पैसे देना जारी रख सकते हैं?",
    choices=yesNoChoice)

    unexpected_increase = models.IntegerField(label="पिछले छह महीनों में अन्य अप्रत्याशित खर्चे (unexpected expenses) कौनसे आये है?", choices=[
    [1, "बच्चों की शिक्षा पर खर्च"],
    [2, "दवाओं या अस्पताल या परीक्षण या संगरोध पर खर्च"],
    [3, "यात्रा पर खर्च"],
    [4, "अन्य"],
    [5, "अप्रत्याशित खर्चा नहीं हुआ"]
])
    savingsbeforelockdown = models.IntegerField(label="लॉकडाउन से पहले आप प्रति माह कितना बचत करना चाहते हैं?", choices=[
    [1, "200-500"],
    [2, "501-1000"],
    [3, "1001-1500"],
    [4, "1501-2000"],
    [5, "2001-2500"],
    [6, "2501-5000"],
    [7, "5001-8000"],
    [8, "8001-10000"],
    [9, "10001 और अधिक"]
])
    howmuchpercentsavingsspent = models.IntegerField(label="लॉकडाउन के दौरान आपके द्वारा बचाए गए धन का कितना प्रतिशत खर्च किया गया था?",
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
    celebratediwali = models.BooleanField(label="क्या आपको लगता है कि आप इस साल दिवाली, ईद या क्रिसमस मनाएंगे?",
                                      choices=yesNoChoice)

    whatwillyouspendon = models.IntegerField(label="आप किस पर खर्च कर सकते हैं?",choices=[[1, "फूड्स"],
                                                                       [2, "बच्चों के लिए कपड़े"],
                                                                       [3, "सबके लिए कपड़े"],
                                                                       [4, "सोना, चांदी, इ"]
                                                                       ])

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
    enoughfoodfortwomeals = models.BooleanField(
    label="क्या अभी घर में सभी के लिए दो वक्त के भोजन के लिए भोजन है?", choices=yesNoChoice)
    howlongcanyouensurefood = models.BooleanField(
    label="यदि लॉकडाउन लंबे समय तक रहता है, तो क्या आपको लगता है कि आपके परिवार को एक दिन में 2 भोजन मिलते रहेंगे?",
    choices=yesNoChoice)
    emergency1000rupees = models.IntegerField(
    label="यदि आपको तत्काल 1000 रुपये की आवश्यकता है, उदाहरण के लिए डॉक्टर की यात्रा के लिए, तो आप इसे कहां पा सकते हैं?",
    choices=[
        [1, "मेरे पास है"],
        [2, "परिवार से पूछ के"],
        [3, "पड़ोसियों या रिश्तेदारों से पूछ के"],
        [4, "ऋणदाता से"],
        [5, "नहीं मिलेगा"],
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
