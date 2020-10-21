from os import environ
#DEBUG=False
SESSION_CONFIGS = [
    dict(
        name='control_marathi',
        display_name='experiment with control - marathi',
        num_demo_participants=1,
        app_sequence=['welcome_screen', 'depression_scale_marathi', 'instruction_display_marathi','instructions_marathi',
                      'control_marathi', 'savings_expense_game', 'SES_marathi'],
    ),
    dict(
        name='hybrid_marathi',
        display_name='experiment with hybrid questions - marathi',
        num_demo_participants=1,
        app_sequence=['welcome_screen', 'depression_scale_marathi', 'instruction_display_marathi','instructions_marathi',
                      'hybrid_marathi', 'savings_expense_game', 'SES_marathi'],
    ),
    dict(
        name='expenditure_anxiety_marathi',
        display_name='experiment with expenditure anxiety - marathi',
        num_demo_participants=1,
        app_sequence=['welcome_screen', 'depression_scale_marathi', 'instruction_display_marathi','instructions_marathi',
                      'expenditureanxiety_marathi', 'savings_expense_game', 'SES_marathi'],
    ),
    dict(
        name='income_uncertainty_marathi',
        display_name='experiment with income uncertainty - marathi',
        num_demo_participants=1,
        app_sequence=['welcome_screen', 'depression_scale_marathi', 'instruction_display_marathi','instructions_marathi',
                      'incomeuncertainty_marathi', 'savings_expense_game', 'SES_marathi'],
    ),
    dict(
        name='expend',
        display_name='expend',
        num_demo_participants=20,
        app_sequence=['savings_expense_game'],
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'mr'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'INR'
USE_POINTS = True

ROOMS = [
    dict(
        name='exp_room',
        display_name='exp_room',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

# don't share this with anybody.
SECRET_KEY = '_l+m7#$h$m32=7rvke^o-nx=eoiz%!#e&d5ut+fw3^qt3$a4yr'

# DEBUG=False

INSTALLED_APPS = [
    'django.contrib.humanize',
    'otree',

]

# inactive session configs
# dict(name='trust', display_name="Trust Game", num_demo_participants=2, app_sequence=['trust', 'payment_info']),
# dict(name='prisoner', display_name="Prisoner's Dilemma", num_demo_participants=2,
#      app_sequence=['prisoner', 'payment_info']),
# dict(name='volunteer_dilemma', display_name="Volunteer's Dilemma", num_demo_participants=3,
#      app_sequence=['volunteer_dilemma', 'payment_info']),
# dict(name='cournot', display_name="Cournot Competition", num_demo_participants=2, app_sequence=[
#     'cournot', 'payment_info'
# ]),
# dict(name='dictator', display_name="Dictator Game", num_demo_participants=2,
#      app_sequence=['dictator', 'payment_info']),
# dict(name='matching_pennies', display_name="Matching Pennies", num_demo_participants=2, app_sequence=[
#     'matching_pennies',
# ]),
# dict(name='traveler_dilemma', display_name="Traveler's Dilemma", num_demo_participants=2,
#      app_sequence=['traveler_dilemma', 'payment_info']),
# dict(name='bargaining', display_name="Bargaining Game", num_demo_participants=2,
#      app_sequence=['bargaining', 'payment_info']),
# dict(name='common_value_auction', display_name="Common Value Auction", num_demo_participants=3,
#      app_sequence=['common_value_auction', 'payment_info']),
# dict(name='bertrand', display_name="Bertrand Competition", num_demo_participants=2, app_sequence=[
#     'bertrand', 'payment_info'
# ]),
# dict(name='public_goods_simple', display_name="Public Goods (simple version from tutorial)",
#      num_demo_participants=3, app_sequence=['public_goods_simple', 'payment_info']),
# dict(name='trust_simple', display_name="Trust Game (simple version from tutorial)", num_demo_participants=2,
#      app_sequence=['trust_simple']),
