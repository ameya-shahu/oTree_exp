
# saving consumption form Strings
PLAYER_CONSUMP_LABEL = "खर्चा :"
PLAYER_BANK_SAVING_LABEL = "बैंक में बचत:"
PLAYER_HOME_SAVING_LABEL = "घर पर बचत:"

PG_MY_TITLE_QUE = 'आपको 10,000 रुपये मिले, आप कितना खर्च करेंगे और आप कितना बचा पाएंगे?'  # update directly in
# template, unused here

PG_MY_FIELD_SUM_GREAT_ERROR = 'आपकी खर्च और कुल बचत 10,000 रुपये से अधिक हैं। खर्च और कुल बचत का कुल 10,000 होना चाहिए।'
PG_MY_FIELD_SUM_LESS_ERROR = 'आपकी खर्च और कुल बचत  10,000 रुपये से कम हैं। खर्च और कुल बचत का कुल 10,000 होना चाहिए ।'

PG_MY_CONSUME_LESS_ERROR = 'आपका खर्च 3000 से कम है। यह खर्च करने के लिए न्यूनतम राशि है।' # edit directly in MyPage.html

# debt choice form strings
PLAYER_DEBTCHOICE_S = [
    'बचत से कुल राशि खर्च करें',
    '{0} प्रति {1}, {2} महीने में पैसा लौटाओ',
]

PLAYER_DEBTCHOICE_LABEL = 'आपने अपने खर्चों को कवर करने के लिए कौन सा विकल्प चुना है?'
PLAYER_FROM_BANK_AMT_LABEL = 'बैंक की बचत से आप कितना पैसा निकालेंगे?'
PLAYER_FROM_HOME_AMT_LABEL = 'आप अपने घर की बचत में से कितना पैसा निकालेंगे?'
PLAYER_LOAN_AMT_LABEL = 'कितना उधार लेंगे?'

PG_DEBTCHOICE_TITLE_QUE = 'आपातकाल के लिए आपको %s रुपये खर्च करने होंगे। आपने कौन सा विकल्प चुना है?'

PG_DEBTCHOICE_LOANSUM_GREAT_ERROR = 'बचत और ऋण का योग अप्रत्याशित खर्चों ({}) के बराबर होना चाहिए।'
PG_DEBTCHOICE_LOANSUM_LESS_ERROR = 'बचत और ऋण का योग अप्रत्याशित खर्चों ({}) के बराबर होना चाहिए।'

PG_DEBTCHOICE_LESS_SAVINGS_ERROR = 'आपकी बचत अप्रत्याशित खर्च ({}) से कम है। आपको उधार लेना चाहिए। बचत और ऋण का योग अप्रत्याशित व्यय ({}) के बराबर होना चाहिए।'

# बचत आणि कर्जाची बेरीज अनपेक्षित खर्चाइतकी असली ा.

# EMI LABELS
EMI_1_LABEL = 'आपके पहले ऋण की ईएमआई {} है'
EMI_2_LABEL = 'आपके दूसरे ऋण की ईएमआई {} है'
EMI_3_LABEL = 'आपके तीसरे ऋण की ईएमआई {} है'

# EMI ERROR
EMI_ERROR = 'आपके पहले ऋण की ईएमआई {} है। आपको इसका भुगतान करना होगा।'

PG_DEBT_LESS_HOME_SAVE_ERROR = 'घर में आपकी बचत आपके द्वारा दर्ज राशि से कम है। कृपया नीचे दिए गए बॉक्स में अपने घर की बचत की जांच करें।'
PG_DEBT_LESS_BANK_SAVE_ERROR = 'बैंक में आपकी बचत दर्ज की गई राशि से कम है। कृपया नीचे दिए गए बॉक्स में अपनी बैंक की बचत की जांच करें।'