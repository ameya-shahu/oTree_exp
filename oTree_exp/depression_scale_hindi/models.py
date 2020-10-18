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
    name_in_url = 'depression_scale_hindi'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # # First Page model
    # name = models.StringField(label='नाव प्रविष्ट करा')
    # age = models.IntegerField(label='आपले वय प्रविष्ट करा')
    # gender = models.StringField(label='आपले लिंग प्रविष्ट करा',
    #                             choices=[['Male', 'पुरुष'],
    #                                      ['female', 'महिला']],
    #                             widget=widgets.RadioSelect, )

    # Second Page model
    sadness = models.IntegerField(
        label='दु: ख:',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मुझे बुरा नहीं लगता ।'],
            [1, 'मुझे अक्सर बुरा लगता है ।'],
            [2, 'मैं हमेशा दुखी रहता हूं ।'],
            [3, 'मैं इतना दुखी या दुखी हूं कि मैं इसे सहन नहीं कर सकता ।']
        ]
    )

    # Third Page model
    pessimistic = models.IntegerField(
        label='निराशावाद: ',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मैं अपने भविष्य में निराश नहीं हूं।'],
            [1, 'मैं अपने भविष्य को लेकर पहले से ज्यादा निराश था। '],
            [2, 'मुझे मेरे लिए काम करने की उम्मीद नहीं है।'],
            [3, 'मुझे लगता है कि मेरा भविष्य अंधकारमय है और केवल खराब होगा।']
        ]
    )

    # Forth Page model
    setbacks = models.IntegerField(
        label='पिछली विफलता: ',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मुझे असफलता का अहसास नहीं है।'],
            [1, 'मैं जितना होना चाहिए था उससे ज्यादा असफल हो गया हूं। '],
            [2, 'जब मैं पीछे मुड़कर देखता हूं, तो मुझे बहुत सारी विफलताएं दिखाई देती हैं।'],
            [3, 'मुझे लगता है कि एक व्यक्ति के रूप में मैं पूरी तरह से विफल हूं।']
        ]
    )

    # Fifth Page model
    lessJoy = models.IntegerField(
        label='आनंद कमी होणे',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मुझे खुशी है कि मुझे चीजों का आनंद लेना है जितना मैंने किया है।'],  # anomaly
            [1, 'मैं पहले जैसी चीजों का आनंद नहीं लेता हूं।'],
            [2, 'मैं उन चीजों से बहुत खुश हूं जो मुझे पसंद हैं।'],
            [3, 'मुझे उन चीज़ों से खुशी नहीं मिल सकती जो मुझे पसंद हैं।']
        ]
    )

    # Sixth Page model
    guilty = models.IntegerField(
        label='अपराधबोध की भावना : ',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मैं विशेष रूप से दोषी महसूस नहीं करता।'],
            [1, 'मैं कई चीजों के बारे में दोषी महसूस करता हूं जो मैंने किया है या करना चाहिए था।'],
            [2, 'ज्यादातर समय मैं दोषी महसूस करता हूं। '],
            [3, 'मुझे हर बार दोषी लगता है।']
        ]
    )

    # seventh page model
    toBePunished = models.IntegerField(
        label='दण्ड की भावना:',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मुझे ऐसा नहीं लगता कि मुझे सजा दी जा रही है। '],
            [1, 'मुझे लगता है कि मुझे सजा दी जा सकती है।'],
            [2, 'मुझे सजा मिलने की उम्मीद है|'],
            [3, 'मैं मैं की तरह मैं दंडित किया जा रहा है लग रहा है।']  # anomaly
        ]
    )

    # eight page model
    selfDoubt = models.IntegerField(
        label='स्वयं की प्रशंसा:',  # anomaly
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मैं हमेशा की तरह मेरे बारे में ऐसा ही महसूस करता हूं।'],
            [1, 'मैंने अपना आत्मविश्वास खो दिया है।'],
            [2, 'मैं अपने आप में निराश हूं।'],
            [3, 'मैं अपने जैसा नहीं हूं।']
        ]
    )

    # ninth page model
    selfCriticism = models.IntegerField(
        label='आत्म-आलोचना',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मैं सामान्य से अधिक आलोचना या दोष नहीं देता।'],
            [1, 'मैं पहले से ज्यादा आलोचना करता हूं। '],
            [2,
             'मैं अपने सभी दोषों के लिए खुद की आलोचना करता हूं। जो कुछ भी होता है, उसके लिए मैं खुद को दोषी मानता हूं।'],
        ]
    )

    # tenth page model
    crying = models.IntegerField(
        label='रोना:',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मैं अब और नहीं रो रहा हूं।'],
            [1, 'मैं पहले से ज्यादा रोता हूं।'],
            [2, 'मैं हर छोटी चीज पर चिल्लाता हूं।'],
            [3, 'मुझे रोने का मन हो रहा है , लेकिन मैं नहीं कर सकता।']
        ]
    )

    # eleventh page model
    protest = models.IntegerField(
        label='आंदोलन',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मैं सामान्य से अधिक परेशान या घायल नहीं हूं।'],
            [1, 'मैं पहले से ज्यादा परेशान या घायल हूं। '],
            [2, 'मैं इतना परेशान या परेशान हूं , फिर भी रहना मुश्किल है।'],
            [3, 'मैं इतना परेशान या चिड़चिड़ा हूँ कि मुझे कुछ हिलाने या करने की आवश्यकता है।']
        ]
    )

    # twelfth page model
    interestLoss = models.IntegerField(
        label='ब्याज की हानि:',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मुझे अन्य लोगों या काम में कोई दिलचस्पी नहीं है। '],
            [1, 'मुझे पहले की तुलना में अन्य लोगों या चीजों में कम दिलचस्पी है। '],
            [2, 'मुझे दूसरे लोगों या चीजों में सबसे ज्यादा दिलचस्पी थी।'],
            [3, 'किसी भी चीज़ में दिलचस्पी लेना मुश्किल है।']
        ]
    )

    # thirteenth page model
    uncertainty = models.IntegerField(
        label='अनिश्चितता',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मैं हमेशा की तरह निर्णय लेता हूं।'],
            [1, 'मुझे सामान्य से अधिक निर्णय लेने में मुश्किल होती है।'],
            [2, 'मुझे पहले से कहीं अधिक निर्णय लेने में कठिनाई होती है। '],
            [3, 'मुझे कोई भी निर्णय लेना मुश्किल है।']
        ]
    )

    # fourteenth page model
    unemployment = models.IntegerField(
        label='बेरोजगारी',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मुझे नहीं लगता कि मैं बेकार हूं।'],
            [1, 'मैं खुद को पहले की तरह उपयोगी और उपयोगी नहीं मानता। '],
            [2, 'मैं दूसरों की तुलना में अधिक अक्षम महसूस करता हूं।.'],
            [3, 'मैं पूरी तरह से बेकार महसूस करता हूं।.']
        ]
    )

    # fifteenth page model
    lessEnergetic = models.IntegerField(
        label='ऊर्जा की हानि:',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मेरे पास सामान्य ऊर्जा है।'],
            [1, 'मेरे पास पहले की तुलना में कम ऊर्जा है।'],
            [2, 'मुझे बहुत कुछ करने की ताकत नहीं है। '],
            [3, 'मेरे पास कुछ भी करने की शक्ति नहीं है।']
        ]
    )

    # sixteenth page model
    sleepPattern = models.IntegerField(
        label='नींद के पैटर्न में बदलाव:',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मैंने नींद में किसी भी बदलाव का अनुभव नहीं किया है। '],
            [1, 'ए मैं सामान्य से कुछ अधिक सोता हूं।'],
            [1, 'बी मैं सामान्य से कुछ कम सोता हूं।'],
            [2, 'ए मैं सामान्य से अधिक सोता हूं।'],
            [2, 'बी मैं सामान्य से बहुत कम सोता हूं।'],
            [3, 'मैं पूरे दिन सोता हूं ।'],
            [3, 'बी मैं 1-2 घंटे जल्दी उठता और सोने के लिए वापस नहीं जा सकते हैं।'],
        ]
    )

    # seventeenth page model
    irritation = models.IntegerField(
        label='चिड़चिड़ापन',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मैं सामान्य से अधिक चिड़चिड़ा नहीं हूं।'],
            [1, 'मैं पहले से ज्यादा चिड़चिड़ा हूं।'],
            [2, 'मैं सामान्य से अधिक चिड़चिड़ा हूं।'],
            [3, 'मुझे हमेशा चिढ़ होती है।'],
        ]
    )

    # eighteenth page model
    hunger = models.IntegerField(
        label='भूख में परिवर्तन:',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मैंने अपनी भूख में कोई बदलाव नहीं देखा।'],
            [1, 'ए हमेशा से मेरी भूख से कुछ कम है'],
            [1, 'बी मेरी भूख सामान्य से थोड़ी अधिक है।'],
            [2, 'अ मेरी भूख पहले की तुलना में बहुत कम है।'],
            [2, 'बी मेरी भूख सामान्य से  कहीं ज्यादा है।'],
            [3, 'ए मुझे कोई भूख नहीं है।'],
            [3, 'बी मैं हमेशा खावसी खाना सोचता हूं।'],  # anomaly
        ]
    )

    # nineteenth page model
    concentration = models.IntegerField(
        label='एकाग्रता की कठिनाई:',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मैं हमेशा की तरह ध्यान केंद्रित कर सकता हूं।'],
            [1, 'मैं हमेशा की तरह ध्यान केंद्रित नहीं कर सकता। '],
            [2, 'लंबे समय तक मेरे दिमाग पर नजर रखना मुश्किल है।'],
            [3, 'मुझे लगता है कि मैं कुछ भी पर ध्यान केंद्रित नहीं कर सकते हैं।'],
        ]
    )

    # twentieth page model
    tiredness = models.IntegerField(
        label='थकान:',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मैं सामान्य से थका या थका नहीं हूं।'],
            [1, 'मैं पहले से कहीं अधिक आसानी से थका हुआ या थका हुआ हूं।'],
            [2, 'मैं बहुत थक गया हूँ या उन चीजों को करने के लिए थक गया हूँ जो मैंने पहले की हैं।'],
            [3, 'मैं उन चीजों को करने के लिए बहुत थक गया हूँ जो मैंने पहले की हैं।'],
        ]
    )
