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
        # label='दु: ख:',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मुझे बुरा नहीं लगता ।'],
            [1, 'मुझे अक्सर बुरा लगता है ।'],
            [2, 'मैं हमेशा दुखी रहता हूं ।'],
            [3, 'मैं इतना दुखी हूं कि मैं इसे सहन नहीं कर सकता ।']
        ]
    )

    # Third Page model
    pessimistic = models.IntegerField(
        # label='निराशावाद: ',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मैं अपने भविष्य को लेकर निराश नहीं हूं।'],
            [1, 'मैं अपने भविष्य को लेकर पहले से ज्यादा निराश था। '],
            [2, 'मुझे लगता है कि मुझे आगे देखने के लिए कुछ भी नहीं है।'],
            [3, 'मुझे लगता है कि मेरा भविष्य अंधकारमय है और केवल खराब होगा।']
        ]
    )

    # Forth Page model
    setbacks = models.IntegerField(
        # label='पिछली विफलता: ',
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
        # label='आनंद कमी होणे',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मुझे चीजों से उतनी ही संतुष्टि मिलती है, जितनी मुझे मिलती थी।'],  # anomaly
            [1, 'मैं चीजों का आनंद नहीं लेता जिस तरह से मैं करता था।'],
            [2, 'मुझे अब किसी भी चीज़ से वास्तविक संतुष्टि नहीं मिलती है'],
            [3, 'मैं असंतुष्ट हूं या हर चीज से ऊब चुका हूं।']
        ]
    )

    # Sixth Page model
    guilty = models.IntegerField(
        # label='अपराधबोध की भावना : ',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मैं विशेष रूप से दोषी महसूस नहीं करता।'],
            [1, 'मैं कई चीजों के बारे में दोषी महसूस करता हूं'],
            [2, 'ज्यादातर समय मैं दोषी महसूस करता हूं। '],
            [3, 'मुझे हर बार दोषी लगता है।']
        ]
    )

    # seventh page model
    toBePunished = models.IntegerField(
        # label='दण्ड की भावना:',
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
        # label='स्वयं की प्रशंसा:',  # anomaly
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मैं अपने आप में निराश महसूस नहीं करता।'],
            [1, 'ममैं अपने आप में निराश हूं।'],
            [2, 'मुझे खुद से घृणा है।'],
            [3, 'मुझे खुद से नफरत है']
        ]
    )

    # ninth page model
    selfCriticism = models.IntegerField(
        # label='आत्म-आलोचना',
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
        # label='रोना:',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मैं किसी भी सामान्य से अधिक नहीं रोता।'],
            [1, 'मैं जितना रोता था, उससे कहीं ज्यादा अब रोता हूं।'],
            [2, 'मैं अब हर समय रोता हूं।'],
            [3, 'मैं रोने में सक्षम हुआ करता था, लेकिन अब मैं चाहकर भी रो नहीं सकता।']
        ]
    )

    # eleventh page model
    protest = models.IntegerField(
        # label='आंदोलन',
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
        # label='ब्याज की हानि:',
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
        # label='अनिश्चितता',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मैं हमेशा की तरह निर्णय लेता हूं।'],
            [1, 'मै निर्णय लेना तालता हू'],
            [2, 'मुझे पहले से कहीं अधिक कठिनाई होती है निर्णय लेने में ।'],
            [3, 'मैं अब और निर्णय नहीं ले सकता।']
        ]
    )

    # fourteenth page model
    unemployment = models.IntegerField(
        # label='बेरोजगारी',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मैं पहले की तरह ही काम कर सकता हूं'],
            [1, 'मयह कुछ करने की शुरुआत करने के लिए एक अतिरिक्त (extra) प्रयास लगता है।'],
            [2, 'मुझे कुछ भी करने के लिए खुद को बहुत मुश्किल से धकेलना पड़ता है।'],
            [3, 'ममैं कोई काम नहीं कर सकता।']
        ]
    )

    # fifteenth page model
    lessEnergetic = models.IntegerField(
        # label='ऊर्जा की हानि:',
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
        # label='नींद के पैटर्न में बदलाव:',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मैंने नींद में किसी भी बदलाव का अनुभव नहीं किया है। '],
            [1, 'मैं सामान्य से कुछ अधिक सोता हूं।'],
            [2, 'मैं सामान्य से कुछ कम सोता हूं।'],
            [3, 'मैं सामान्य से अधिक सोता हूं।'],
            [4, 'मैं सामान्य से बहुत कम सोता हूं।'],
            [5, 'मैं पूरे दिन सोता हूं ।'],
            [6, 'बी मैं 1-2 घंटे जल्दी उठता और सोने के लिए वापस नहीं जा सकते हैं।'],
        ]
    )

    # seventeenth page model
    irritation = models.IntegerField(
        # label='चिड़चिड़ापन',
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
        # label='भूख में परिवर्तन:',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मैंने अपनी भूख में कोई बदलाव नहीं देखा।'],
            [1, 'हमेशा से मेरी भूख से कुछ कम है।'],
            [2, 'मेरी भूख सामान्य से थोड़ी अधिक है।'],
            [3, 'मेरी भूख पहले की तुलना में बहुत कम है।'],
            [4, 'मेरी भूख सामान्य से  कहीं ज्यादा है।'],
            [5, 'मुझे कोई भूख नहीं है।'],
            [6, 'मैं हमेशा खावसी खाना सोचता हूं।'],  # anomaly
        ]
    )

    # nineteenth page model
    concentration = models.IntegerField(
        # label='एकाग्रता की कठिनाई:',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मैं हमेशा की तरह ध्यान केंद्रित कर सकता हूं।'],
            [1, 'मैं हमेशा की तरह ध्यान केंद्रित नहीं कर सकता। '],
            [2, 'लंबे समय तक मेरा ध्यान केन्द्रित करना मुश्किल है।'],
            [3, 'मुझे लगता है कि मैं कुछ भी पर ध्यान केंद्रित नहीं कर सकते हू।'],
        ]
    )

    # twentieth page model
    tiredness = models.IntegerField(
        # label='थकान:',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मैं सामान्य से थका या थका नहीं हूं।'],
            [1, 'मैं पहले से कहीं अधिक आसानी से थका हुआ या थका हुआ हूं।'],
            [2, 'मैं बहुत थक गया हूँ या उन चीजों को करने के लिए थक गया हूँ जो मैंने पहले की हैं।'],
            [3, 'मैं उन चीजों को करने के लिए बहुत थक गया हूँ जो मैंने पहले की हैं।'],
        ]
    )
