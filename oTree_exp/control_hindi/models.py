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
    name_in_url = 'control_hindi'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


yesNoChoice = [
    [True, 'हाँ'],
    [False, 'नहीं'],
]


class Player(BasePlayer):
    doyouwatchbollywood = models.BooleanField(label="क्या आप बॉलीवुड फिल्में देखते हैं?", choices=yesNoChoice)
    favactor1 = models.IntegerField(label="अपना पसंदीदा अभिनेता चुनें:", choices=[[1, "शाहरुख खान"], [2, "सलमान खान"]])
    favactor2 = models.IntegerField(label="अपना पसंदीदा अभिनेता चुनें:", choices=[[1, "अजय देवगण"], [2, "अक्षय कुमार"]])
    favactor3 = models.IntegerField(label="अपना पसंदीदा अभिनेता चुनें:", choices=[[1, "आमिर खान"], [2, "सलमान खान"]])
    favactor4 = models.IntegerField(label="अपना पसंदीदा अभिनेता चुनें:", choices=[[1, "आमिर खान"], [2, "शाहरुख खान"]])
    favactor5 = models.IntegerField(label="अपना पसंदीदा अभिनेता चुनें:", choices=[[1, "सुनील शेट्टी"], [2, "शाहरुख खान"]])
    favactress1 = models.IntegerField(label="अपनी पसंदीदा अभिनेत्री को चुनें:",
                                      choices=[[1, "काजोल"], [2, "राणी मुखर्जी"]])
    favactress2 = models.IntegerField(label="अपनी पसंदीदा अभिनेत्री को चुनें:",
                                      choices=[[1, "माधुरी दीक्षित"], [2, "रवीना टंडन"]])
    favactress3 = models.IntegerField(label="अपनी पसंदीदा अभिनेत्री को चुनें:",
                                      choices=[[1, "माधुरी दीक्षित"], [2, "शिल्पा शेट्टी"]])
    favmovie1 = models.IntegerField(label="अपनी पसंदीदा फिल्म चुनें:",
                                    choices=[[1, "हम आपके हैं कौन"], [2, "अंदाज अपना अपना"]])
    favmovie2 = models.IntegerField(label="अपनी पसंदीदा फिल्म चुनें:",
                                    choices=[[1, "कभी खुशी कभी गम"], [2, "कल हो ना हो"]])
    favmovie3 = models.IntegerField(label="अपनी पसंदीदा फिल्म चुनें:",
                                    choices=[[1, "कुछ कुछ होता है"], [2, "कभी खुशी कभी गम"]])
    doyoulikesongs = models.BooleanField(label="क्या आपको बॉलीवुड गाने पसंद हैं?", choices=yesNoChoice)
    favsinger1 = models.IntegerField(label="अपनी पसंदीदा महिला गायिका चुनें:",
                                     choices=[[1, "अलका याज्ञिक"], [2, "साधना सरगम"]])
    favsinger2 = models.IntegerField(label="अपनी पसंदीदा महिला गायिका चुनें:",
                                     choices=[[1, "सुनिधी चौहान"], [2, "श्रेया घोषाल"]])
    favsinger3 = models.IntegerField(label="अपनी पसंदीदा गायक चुनें:",
                                     choices=[[1, "उदित नारायण"], [2, "कुमार सानू"]])
    favsinger4 = models.IntegerField(label="अपना पसंदीदा महिला गायिका चुनें:", choices=[[1,"लता मंगेशकर"],[2, "आशा भोंसले"]])
    favsinger5 = models.IntegerField(label="अपना पसंदीदा गायक चुनें:", choices=[[1,"किशोर कुमार"],[2, "मोहम्मद रफी"]])
    favsinger6 = models.IntegerField(label="अपना पसंदीदा गायक चुनें:", choices=[[1,"किशोर कुमार"],[2, "सुरेश वाडकर"]])
    music1990sor2000s = models.IntegerField(label="क्या आपको 1990s का संगीत या 2000s का संगीत पसंद है?",
                                            choices=[[1, "1990s"], [2, "2000s"]])
    sloworfastmusic = models.IntegerField(label="क्या आपको नृत्य गाने या धीमे गाने पसंद हैं?",
                                          choices=[[1, "नृत्य गाने"], [2, "धीमे गाने"]])
    doyouwatchtv = models.BooleanField(label="क्या आप टीवी सेरिअल्स देखते हैं?", choices=yesNoChoice)
    onlineorontv = models.IntegerField(label="आप हिंदी सेरिअल्स देखते हैं या मराठी?",
                                       choices=[[1, "हिंदी"], [2, "मराठी"]])
    lasttvshow = models.IntegerField(label="आपके द्वारा देखा गया नवीनतम टीवी शो क्या है?",
                                     choices=[[1, "सॅक्रेड गेम्स "],
                                              [2, "पाताल लोक"],
                                              [3, "फॅमिली मॅन"], [4,
                                                                  "इनमे से कोई भी नहीं"]])
    howmuchyouliked = models.IntegerField(label="आप जो सेरिअल्स देखते हैं, उससे आपको कितना पसंद है उसको ०-३ में रेट कीजिये",
                                          choices=[0, 1, 2, 3])
    optimistic = models.IntegerField(label="0-3 पर, आप अपने भविष्य को लेकर कितने आशावादी हैं?",
                                     choices=[0, 1, 2, 3])
