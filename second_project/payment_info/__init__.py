from otree.api import *
import re
import random

doc = """
reflect the payment in the end
"""


class C(BaseConstants):
    NAME_IN_URL = 'payment_info'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    round_to_pay1 = models.StringField()
    role_to_pay1 = models.StringField()
    points_to_pay1 = models.StringField()
    round_to_pay2 = models.StringField()
    role_to_pay2 = models.StringField()
    points_to_pay2 = models.StringField()
    points_to_pay3 = models.IntegerField()
    points_to_pay4 = models.IntegerField()
    points_to_pay = models.StringField()
    block_to_pay = models.IntegerField()
    round_to_pay = models.StringField()
    role_to_pay = models.StringField()
    Gender =  models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[
            [0, 'Male'],
            [1, 'Female'],
            [2, 'Prefer not to say'],
        ]
    )
    Major = models.StringField()
    Age = models.StringField()
    How_choose = models.StringField()

class Survey(Page):
    form_model = 'player'
    form_fields = ['Gender', 'Age', 'Major', 'How_choose']
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        player.round_to_pay1 = str(participant.vars['DG'][2])
        player.role_to_pay1 = str(participant.vars['DG'][1])
        player.points_to_pay1 = str(participant.vars['DG'][0])
        player.points_to_pay3 = int(re.findall('\d+', player.points_to_pay1)[0])
        player.round_to_pay2 = str(participant.vars['ASPD'][2])
        player.role_to_pay2 = str(participant.vars['ASPD'][1])
        player.points_to_pay2 = str(participant.vars['ASPD'][0])
        player.points_to_pay4 = int(re.findall('\d+', player.points_to_pay2)[0])


        block = random.randint(1, 2)
        player.block_to_pay = block
        if block == 1:
            player.points_to_pay = player.points_to_pay1
            player.payoff = 0 - player.points_to_pay4
            player.round_to_pay = player.round_to_pay1
            player.role_to_pay = player.role_to_pay1
        elif block == 2:
            player.points_to_pay = player.points_to_pay2
            player.payoff = 0 - player.points_to_pay3
            player.round_to_pay = player.round_to_pay2
            player.role_to_pay = player.role_to_pay2



class Payment(Page):
    pass


page_sequence = [Survey, Payment]
