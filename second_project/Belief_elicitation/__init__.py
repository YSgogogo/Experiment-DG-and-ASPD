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

    timeSpentm1 = models.FloatField()
    timeSpentm2 = models.FloatField()
    timeSpentr1 = models.FloatField()
    timeSpentr2 = models.FloatField()
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
    f7 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%-20%"), (1, "21%-40%"), (2, "41%-60%"), (3, "61%-80%"),(4, "81%-100%")],
    )
    f8 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%-20%"), (1, "21%-40%"), (2, "41%-60%"), (3, "61%-80%"),(4, "81%-100%")],
    )
    f9 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%-20%"), (1, "21%-40%"), (2, "41%-60%"), (3, "61%-80%"),(4, "81%-100%")],
    )
    f10 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%-20%"), (1, "21%-40%"), (2, "41%-60%"), (3, "61%-80%"),(4, "81%-100%")],
    )
    f11 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%-20%"), (1, "21%-40%"), (2, "41%-60%"), (3, "61%-80%"),(4, "81%-100%")],
    )
    f12 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%-20%"), (1, "21%-40%"), (2, "41%-60%"), (3, "61%-80%"),(4, "81%-100%")],
    )
    f13 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%-20%"), (1, "21%-40%"), (2, "41%-60%"), (3, "61%-80%"),(4, "81%-100%")],
    )
    f14 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%-20%"), (1, "21%-40%"), (2, "41%-60%"), (3, "61%-80%"),(4, "81%-100%")],
    )
    f15 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%-20%"), (1, "21%-40%"), (2, "41%-60%"), (3, "61%-80%"),(4, "81%-100%")],
    )
    f16 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%-20%"), (1, "21%-40%"), (2, "41%-60%"), (3, "61%-80%"),(4, "81%-100%")],
    )


class monotone1(Page):
    form_model = 'player'
    form_fields = ['f1', 'f2', 'f3', 'f4', 'timeSpentm1']
    timer_text = 'Time remaining:'

class monotone2(Page):
    form_model = 'player'
    form_fields = ['f5', 'f6', 'f7', 'f8', 'timeSpentm2']
    timer_text = 'Time remaining:'

class reciprocal1(Page):
    form_model = 'player'
    form_fields = ['f9', 'f10', 'f11', 'f12', 'timeSpentr1']
    timer_text = 'Time remaining:'

class reciprocal2(Page):
    form_model = 'player'
    form_fields = ['f13', 'f14', 'f15', 'f16', 'timeSpentr2']
    timer_text = 'Time remaining:'

page_sequence = [monotone1, monotone2, reciprocal1, reciprocal2]