from os import environ


SESSION_CONFIGS = [
    dict(
        name='Our_experiment',
        display_name="Our experiment (2 players)",
        app_sequence=['DG', 'ASPD', 'Belief_elicitation', 'payment_info'],
        num_demo_participants=2,
    ),
    dict(
        name='Experiment',
        display_name="Our experiment (4 players)",
        app_sequence=['DG', 'ASPD', 'Belief_elicitation', 'payment_info'],
        num_demo_participants=4,
    ),
]


SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.01, participation_fee=5.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []


LANGUAGE_CODE = 'en'


REAL_WORLD_CURRENCY_CODE = 'GBP'
USE_POINTS = True
POINTS_CUSTOM_NAME = 'tokens'

ROOMS = [
    dict(
        name='Eco_experiment',
        display_name='Essex Lab',
        participant_label_file='_EssexLab/Eco.txt',
    ),
]

ADMIN_USERNAME = 'admin'

ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Let us play games.
"""


SECRET_KEY = '9524096400431'

INSTALLED_APPS = ['otree']


SESSION_FIELDS = [
    'completions_by_treatment',
    'past_groups',
    'matrices',
    'wait_for_ids',
    'arrived_ids',
]

PARTICIPANT_FIELDS = [
    'app_payoffs',
    'expiry',
    'finished_rounds',
    'language',
    'num_rounds',
    'partner_history',
    'past_group_id',
    'progress',
    'quiz_num_correct',
    'selected_round',
    'task_rounds',
    'time_pressure',
    'wait_page_arrival',
    'selected_round',
]