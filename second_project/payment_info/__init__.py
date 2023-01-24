from otree.api import *


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

class Pay(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        player.round_to_pay1 = str(participant.vars['DG'][2])
        player.role_to_pay1 = str(participant.vars['DG'][1])
        player.points_to_pay1 = str(participant.vars['DG'][0])



class Results1(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        player.round_to_pay2 = str(participant.vars['ASPD'][2])
        player.role_to_pay2 = str(participant.vars['ASPD'][1])
        player.points_to_pay2 = str(participant.vars['ASPD'][0])

class Results2(Page):
    pass


page_sequence = [Pay, Results1, Results2]
