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
    name_in_url = 'instructions_quiz_hindi'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    instructionquestion1 = models.IntegerField(label="खेल कितने राउंड का है?", choices=[[1, "10"],
                                                                                        [2, "15"],
                                                                                        [3, "16"],
                                                                                        [4, "20"]])
    instructionquestion2 = models.IntegerField(label="प्रत्येक राउंड में आपको कितना पैसा मिलेगा?",
                                               widget=widgets.RadioSelect,
                                               choices=[[1, "5000"], [2, "10000"],
                                                        [3, "15000"], [4, "25000"]])
    instructionquestion3 = models.IntegerField(label="आप खर्चों का भुगतान कैसे कर सकते हैं?",
                                               widget=widgets.RadioSelect,
                                               choices=[[1, "बचत"], [2, "कर्ज"], [3, "दोनों"], [4, "दोनों भी नहीं"]])
    instructionquestion4 = models.IntegerField(
        label="आदर्श हप्तापेक्षा तुम्हाला किती वेळा कमी पैसे देण्याची परवानगी आहे?",
        choices=[1, 2, 3, 4])
    instructionquestion5 = models.IntegerField(label="आपण कमी पैसे दिल्यास आदर्श हप्ताचे काय होते?",
                                               widget=widgets.RadioSelect,
                                               choices=[[1, "काहीही होत नाही"], [2, "ते पुन्हा कॅलक्यूलेट जाते"]])
    instructionquestion6 = models.IntegerField(
        label="नवीन आदर्श हप्ता फक्त पुढील फेरीसाठी लागू आहे की त्यानंतरच्या सर्व फेऱयांसाठी?",
        widget=widgets.RadioSelect,
        choices=[[1, "फक्त पुढील फेरीसाठी"], [2, "त्यानंतरच्या सर्व फेऱयांसाठी"]])
    instructionquestion7 = models.IntegerField(
        label="तुम्ही 3 वेळा आदर्श गुंतवणूकीपेक्षा कमी पैसे दिल्यानंतर काय होईल?",
        widget=widgets.RadioSelect,
        choices=[[1, "काहीही होणार नाही"], [2, "कर्ज गोठेल"]])
    instructionquestion8 = models.IntegerField(label="खूप कर्ज असेल आणि परतफेड करण्याचा कालावधी संपल्यावर काय होईल?",
                                               widget=widgets.RadioSelect,
                                               choices=[[1, "काहीही होणार नाही"], [2, "कर्ज गोठेल"]])
    instructionquestion9 = models.IntegerField(label="आपके भुगतान की गणना कैसे की जाती है?",
                                               widget=widgets.RadioSelect,
                                               choices=[[1, "कुल बचत"],
                                                        [2, "कुल बकाया कर्ज"],
                                                        [3, "कुल बचत से घटाए गए कुल ऋण के बाद शेष राशि"]])
