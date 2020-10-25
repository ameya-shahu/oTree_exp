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
    name_in_url = 'control_marathi'
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
    doyouwatchbollywood=models.BooleanField(label="आपण बॉलिवूड म्हणजे हिंदी सिनेमे पाहता का?", choices=yesNoChoice)
    favactor1=models.IntegerField(label="तुमचा आवडता अभिनेता निवडा:",choices=[[1,"शाहरुख खान"],[2,"सलमान खान"]])
    favactor2 = models.IntegerField(label="तुमचा आवडता अभिनेता निवडा:", choices=[[1, "अजय देवगण"], [2, "अक्षय कुमार"]])
    favactor3 = models.IntegerField(label="तुमचा आवडता अभिनेता निवडा:", choices=[[1, "आमिर खान"], [2, "सलमान खान"]])
    favactor4 = models.IntegerField(label="तुमचा आवडता अभिनेता निवडा:", choices=[[1, "आमिर खान"], [2, "शाहरुख खान"]])
    favactor5 = models.IntegerField(label="तुमचा आवडता अभिनेता निवडा:", choices=[[1, "सुनील शेट्टी"], [2, "शाहरुख खान"]])
    favactress1 = models.IntegerField(label="तुमचा आवडती अभिनेत्री निवडा:", choices=[[1, "काजोल"], [2, "राणी मुखर्जी"]])
    favactress2 = models.IntegerField(label="तुमचा आवडती अभिनेत्री निवडा:", choices=[[1, "माधुरी दीक्षित"], [2, "रवीना टंडन"]])
    favactress3 = models.IntegerField(label="तुमचा आवडती अभिनेत्री निवडा:", choices=[[1, "माधुरी दीक्षित"], [2, "शिल्पा शेट्टी"]])
    favmovie1=models.IntegerField(label="तुमचा आवडता चित्रपट निवडा:",choices=[[1,"हम आपके हैं कौन"],[2,"अंदाज अपना अपना"]])
    favmovie2=models.IntegerField(label="तुमचा आवडता चित्रपट निवडा:",choices=[[1,"कभी खुशी कभी गम"],[2,"कल हो ना हो"]])
    favmovie3=models.IntegerField(label="तुमचा आवडता चित्रपट निवडा:",choices=[[1,"कुछ कुछ होता है"],[2,"कभी खुशी कभी गम"]])
    doyoulikesongs=models.BooleanField(label=" हिंदी गाणी तुम्हाला आवडतात का?",choices=yesNoChoice)
    favsinger1=models.IntegerField(label="आपल्या आवडत्या गायकाची निवड कराः:", choices=[[1,"अलका याज्ञिक"],[2, "साधना सरगम"]])
    favsinger2=models.IntegerField(label="आपल्या आवडत्या गायकाची निवड कराः:", choices=[[1,"सुनिधी चौहान"],[2, "श्रेया घोषाल"]])
    favsinger3=models.IntegerField(label="आपल्या आवडत्या गायकाची निवड कराः:", choices=[[1,"उदित नारायण"],[2, "कुमार सानू"]])
    favsinger4=models.IntegerField(label="आपल्या आवडत्या गायकाची निवड कराः:", choices=[[1,"लता मंगेशकर"],[2, "आशा भोंसले"]])
    favsinger5=models.IntegerField(label="आपल्या आवडत्या गायकाची निवड कराः:", choices=[[1,"किशोर कुमार"],[2, "मोहम्मद रफी"]])
    favsinger6=models.IntegerField(label="आपल्या आवडत्या गायकाची निवड कराः:", choices=[[1,"किशोर कुमार"],[2, "सुरेश वाडकर"]])
    music1990sor2000s=models.IntegerField(label="आपल्याला 1990s चे संगीत आवडते कि 2000s चे संगीत?", choices=[[1,"1990s"],[2,"2000s"]])
    sloworfastmusic=models.IntegerField(label="आपल्याला नृत्य गाणे आवडतात का मंद गाणे?",choices=[[1,"नृत्य गाणे"],[2,"मंद गाणे"]])
    doyouwatchtv=models.BooleanField(label="आपण टीव्ही मालिका पाहता का?",choices=yesNoChoice)
    onlineorontv=models.IntegerField(label="आपण हिंदी मालिका बघता कि मराठी?",choices=[[1,"हिंदी"],[2,"मराठी"]])
    lasttvshow=models.IntegerField(label="आपण पाहिलेला नवीनतम टीव्ही शो कोणता आहे?",choices=[[1,"सॅक्रेड गेम्स "],
    [2, "पाताल लोक"],[3, "फॅमिली मॅन"], [4, "वरीलपैकी काहीही नाही"]])
    howmuchyouliked=models.IntegerField(label="तुम्ही जी मालिका बघता ती तुम्हाला किती आवडते ते 0 ते 3 पर्यंत रेट करा.",
                                        choices=[0, 1, 2, 3])
    optimistic = models.IntegerField(label="0-3 च्या प्रमाणात, आपण आपल्या भविष्याबद्दल किती आशावादी आहात?", choices=[0,1,2,3])





