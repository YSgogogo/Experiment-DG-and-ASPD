from otree.api import *
import random
from random import choice

doc = """
player's beliefs
"""

class C(BaseConstants):
    NAME_IN_URL = 'Belief_elicitation'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):


    f1 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%-20%"), (1, "21%-40%"), (2, "41%-60%"), (3, "61%-80%"),(4, "81%-100%")],
    )
    f2 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%-20%"), (1, "21%-40%"), (2, "41%-60%"), (3, "61%-80%"),(4, "81%-100%")],
    )
    f3 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%-20%"), (1, "21%-40%"), (2, "41%-60%"), (3, "61%-80%"),(4, "81%-100%")],
    )
    f4 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%-20%"), (1, "21%-40%"), (2, "41%-60%"), (3, "61%-80%"),(4, "81%-100%")],
    )
    f5 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%-20%"), (1, "21%-40%"), (2, "41%-60%"), (3, "61%-80%"),(4, "81%-100%")],
    )
    f6 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%-20%"), (1, "21%-40%"), (2, "41%-60%"), (3, "61%-80%"),(4, "81%-100%")],
    )

class Second_Mover_cooperate(Page):
    form_model = 'player'
    form_fields = ['f1', 'f2', 'f3']

class Second_Mover_defect(Page):
    form_model = 'player'
    form_fields = ['f4', 'f5', 'f6']


page_sequence = [Second_Mover_cooperate, Second_Mover_defect,]