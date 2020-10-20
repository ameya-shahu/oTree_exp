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

author = 'Ameya Shahu'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'depression_scale_marathi'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
# Second Page model
    sadness = models.IntegerField(
         label='दु: ख:', widget=widgets.RadioSelect,
        choices=[ [0, 'मला वाईट वाटत नाही.'],
                  [1, 'मला बर्‍याच वेळा वाईट वाटते.'],
                  [2, 'मी नेहमीच दु: खी असतो.'],
                  [3, 'मी इतका दु: खी किंवा दुःखी आहे की मी ते सहन करू शकत नाही.']
                  ]
    )

    # Third Page model
    pessimistic = models.IntegerField(
        label='निराशावाद: ',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मी माझ्या भविष्याविषयी निराश नाही.'],
            [1, 'मी माझ्या पूर्वीपेक्षा माझ्या भविष्याबद्दल निराश होतो.'],
            [2, 'माझ्याकडून गोष्टी माझ्यासाठी काम करतील अशी मी अपेक्षा करीत नाही.'],
            [3, ' मला वाटते की माझे भविष्य निराश आहे आणि फक्त आणखी वाईट होईल.']
        ]
    )

    # Forth Page model
    setbacks = models.IntegerField(
        label='मागील अपयश: ',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मला अपयशी वाटत नाही.'],
            [1, 'मी जितके पाहिजे त्यापेक्षा जास्त अयशस्वी झालो आहे.'],
            [2, 'मी मागे वळून पाहताना मला बर्‍याच अपयशी दिसतात.'],
            [3, 'मला वाटते की एक व्यक्ती म्हणून मी पूर्णपणे अपयशी आहे.']
        ]
    )

    # Fifth Page model
    lessJoy = models.IntegerField(
        label='आनंद कमी होणे',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'आपल्या आनंदात ज्या गोष्टी केल्या त्या मला मिळाल्या तितका आनंद मला मिळतो.'],
            [1, 'मी पूर्वीसारख्या गोष्टींचा आनंद घेत नाही.'],
            [2, 'मी ज्या गोष्टींचा आनंद घेत असे त्यापासून मला फारच आनंद होत आहे.'],
            [3, 'मी ज्या गोष्टींचा आनंद घेत असे त्यापासून मला आनंद मिळू शकत नाही.']
        ]
    )

    # Sixth Page model
    guilty = models.IntegerField(
        label='दोषी भावना:',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मला विशेषतः दोषी वाटत नाही.'],
            [1, 'मी केलेल्या अनेक गोष्टी केल्या किंवा केल्या पाहिजेत याबद्दल मला दोषी वाटते.'],
            [2, 'बहुतेक वेळा मला बर्‍यापैकी दोषी वाटते.'],
            [3, 'मला प्रत्येक वेळी दोषी वाटते.']
        ]
    )

    # seventh page model
    # toBePunished = models.IntegerField(
    #     label='शिक्षेची भावना:',
    #     widget=widgets.RadioSelect,
    #     choices=[
    #         [0, 'मला असे वाटत नाही की मला शिक्षा होत आहे.'],
    #         [1, 'मला असे वाटते की मला शिक्षा होऊ शकते.'],
    #         [2, 'मला शिक्षा होण्याची अपेक्षा आहे.'],
    #         [3, 'मला असे वाटते की मला शिक्षा होत आहे.']
    #     ]
    # )

    # eight page model
    selfDoubt = models.IntegerField(
        label='स्वत: ची नापसंती :',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मला माझ्याबद्दलही नेहमीसारखंच वाटतं.'],
            [1, 'माझा माझा आत्मविश्वास उडाला आहे.'],
            [2, 'मी स्वतःमध्ये निराश आहे.'],
            [3, 'मी स्वतःला आवडत नाही.']
        ]
    )

    # ninth page model
    # selfCriticism = models.IntegerField(
    #     label='स्वत: ची टीका:',
    #     widget=widgets.RadioSelect,
    #     choices=[
    #         [0, 'मी नेहमीपेक्षा टीका किंवा दोष देत नाही.'],
    #         [1, 'मी माझ्यापेक्षा पूर्वीपेक्षा जास्त टीका करतो.'],
    #         [2, 'माझ्या सर्व दोषांबद्दल मी माझ्यावर टीका करतो. जे घडते त्या सर्व गोष्टींसाठी मी स्वत: ला दोषी ठरवितो.'],
    #     ]
    # )

    # tenth page model
    crying = models.IntegerField(
        label='रडणे:',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मी पूर्वीपेक्षा रडत नाही.'],
            [1, 'मी पूर्वीपेक्षा जास्त रडतो.'],
            [2, 'मी प्रत्येक छोट्या छोट्या गोष्टीवर ओरडतो.'],
            [3, 'मला रडण्यासारखे वाटते, पण मला ते शक्य नाही.']
        ]
    )

    # eleventh page model
    # protest = models.IntegerField(
    #     label='आंदोलन',
    #     widget=widgets.RadioSelect,
    #     choices=[
    #         [0, 'मी नेहमीपेक्षा अस्वस्थ किंवा जखमेच्या नाही.'],
    #         [1, 'मला नेहमीपेक्षा जास्त अस्वस्थ वा जखमी झाले आहे.'],
    #         [2, 'मी इतका अस्वस्थ किंवा अस्वस्थ आहे, स्थिर राहणे कठीण आहे.'],
    #         [3, 'मी इतका अस्वस्थ किंवा चिडचिडलो आहे की मला हालचाल करणे किंवा काहीतरी करणे आवश्यक आहे.']
    #     ]
    # )

    # twelfth page model
    # interestLoss = models.IntegerField(
    #     label='व्याज गमावणे:',
    #     widget=widgets.RadioSelect,
    #     choices=[
    #         [0, 'मी इतर लोक किंवा कार्यात रस घेतलेला नाही.'],
    #         [1, 'मला पूर्वीपेक्षा इतर लोकांमध्ये किंवा गोष्टींमध्ये कमी रस आहे.'],
    #         [2, 'माझी इतर लोकांमध्ये किंवा गोष्टींबद्दल मला सर्वाधिक रस वाटला.'],
    #         [3, 'कोणत्याही गोष्टीमध्ये रस घेणे कठीण आहे.']
    #     ]
    # )

    # thirteenth page model
    uncertainty = models.IntegerField(
        label='अनिश्चितता',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मी नेहमीप्रमाणेच निर्णय घेतो.'],
            [1, 'नेहमीपेक्षा निर्णय घेणे मला अधिक अवघड वाटते.'],
            [2, 'मला पूर्वीपेक्षा जास्त निर्णय घेण्यास जास्त अडचण आहे.'],
            [3, 'मला कोणतेही निर्णय घेण्यास त्रास होतो.']
        ]
    )

    # fourteenth page model
    unemployment = models.IntegerField(
        label='बेकारपणा',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मला असे वाटत नाही की मी निरुपयोगी आहे.'],
            [1, 'मी स्वतःला पूर्वीसारखे उपयुक्त आणि उपयुक्त मानत नाही.'],
            [2, 'इतरांच्या तुलनेत मी अधिक नालायक वाटते.'],
            [3, 'मी पूर्णपणे निरुपयोगी वाटते.']
        ]
    )

    # fifteenth page model
    # lessEnergetic = models.IntegerField(
    #     label='उर्जा कमी होणे:',
    #     widget=widgets.RadioSelect,
    #     choices=[
    #         [0, 'माझ्याकडे नेहमीसारखी उर्जा आहे.'],
    #         [1, 'माझ्याकडे पूर्वीपेक्षा कमी ऊर्जा आहे.'],
    #         [2, 'माझ्याकडे खूप करण्याची शक्ती नाही.'],
    #         [3, 'माझ्याकडे काहीही करण्याची शक्ती नाही.']
    #     ]
    # )

    # sixteenth page model
    # sleepPattern = models.IntegerField(
    #     label='झोपेच्या पॅटर्नमध्ये बदल:',
    #     widget=widgets.RadioSelect,
    #     choices=[
    #         [0, 'मला झोपेत कोणताही बदल अनुभवलेला नाही.'],
    #         [1, 'मी नेहमीपेक्षा काही जास्त झोपतो.'],
    #         [2, 'मी नेहमीपेक्षा काहीसे कमी झोपतो.'],
    #         [3, 'मी नेहमीपेक्षा जास्त झोपतो.'],
    #         [4, 'मी नेहमीपेक्षा खूपच कमी झोपतो.'],
    #         [5, 'मी दिवसभर झोपतो.'],
    #         [6, 'मी 1-2 तास लवकर उठतो आणि पुन्हा झोपू शकत नाही. '],
    #     ]
    # )

    # seventeenth page model
    # irritation = models.IntegerField(
    #     label='चिडचिडेपणा ',
    #     widget=widgets.RadioSelect,
    #     choices=[
    #         [0, 'मी नेहमीपेक्षा चिडचिडे नाही'],
    #         [1, 'मी नेहमीपेक्षा चिडचिडे आहे.'],
    #         [2, 'मी नेहमीपेक्षा चिडचिडे आहे.'],
    #         [3, 'मी नेहमी चिडचिडत असतो.'],
    #     ]
    # )

    # eighteenth page model
    # hunger = models.IntegerField(
    #     label='चभूक बदल:',
    #     widget=widgets.RadioSelect,
    #     choices=[
    #         [0, 'मला माझ्या भूकमध्ये कोणताही बदल अनुभवला नाही.'],
    #         [1, 'माझी भूक नेहमीपेक्षा काहीशी कमी आहे.'],
    #         [2, 'माझी भूक नेहमीपेक्षा थोडी जास्त आहे.'],
    #         [3, 'माझी भूक पूर्वीपेक्षा खूपच कमी आहे.'],
    #         [4, 'माझी भूक नेहमीपेक्षा जास्त आहे.'],
    #         [5, 'मला भूक मुळीच नाही.'],
    #         [6, 'मी नेहमी अन्न खावेसे वाटते.'],
    #     ]
    # )

    # nineteenth page model
    concentration = models.IntegerField(
        label='चएकाग्रता अडचण:',
        widget=widgets.RadioSelect,
        choices=[
            [0, 'मी नेहमीप्रमाणेच एकाग्र होऊ शकतो.'],
            [1, 'मी नेहमीप्रमाणेच एकाग्र होऊ शकत नाही.'],
            [2, 'बर्‍याच काळापर्यंत माझ्या मनावर लक्ष ठेवणे कठीण आहे.'],
            [3, 'मला असे वाटते की मी कशावरही लक्ष केंद्रित करू शकत नाही.'],
        ]
    )

    # twentieth page model
    # tiredness = models.IntegerField(
    #     label='थकवा:',
    #     widget=widgets.RadioSelect,
    #     choices=[
    #         [0, 'मी नेहमीपेक्षा थकलेला किंवा थकलेला नाही.'],
    #         [1, 'मी नेहमीपेक्षा अधिक सहजपणे थकलो किंवा थकलो आहे.'],
    #         [2, 'मी पूर्वी करत असलेल्या बर्‍यापैकी गोष्टी करण्यासाठी मी खूप थकलो आहे किंवा थकलो आहे.'],
    #         [3, 'मी पूर्वी करत असलेल्या बर्‍याच गोष्टी करण्यासाठी मी खूप थकलो आहे किंवा थकलो आहे.'],
    #     ]
    # )
