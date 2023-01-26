from otree.api import *


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
        widget=widgets.RadioSelect, choices=[(0, "0%"), (1, "1%-20%"), (2, "21%-40%"), (3, "41%-60%"), (4, "61%-80%"),(5, "81%-99%"), (6, "100%")],
    )
    f2 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%"), (1, "1%-20%"), (2, "21%-40%"), (3, "41%-60%"), (4, "61%-80%"),(5, "81%-99%"), (6, "100%")],
    )
    f3 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%"), (1, "1%-20%"), (2, "21%-40%"), (3, "41%-60%"), (4, "61%-80%"),(5, "81%-99%"), (6, "100%")],
    )
    f4 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%"), (1, "1%-20%"), (2, "21%-40%"), (3, "41%-60%"), (4, "61%-80%"),(5, "81%-99%"), (6, "100%")],
    )
    f5 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%"), (1, "1%-20%"), (2, "21%-40%"), (3, "41%-60%"), (4, "61%-80%"),(5, "81%-99%"), (6, "100%")],
    )
    s1c = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%"), (1, "1%-20%"), (2, "21%-40%"), (3, "41%-60%"), (4, "61%-80%"),(5, "81%-99%"), (6, "100%")],
    )
    s2c = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%"), (1, "1%-20%"), (2, "21%-40%"), (3, "41%-60%"), (4, "61%-80%"),(5, "81%-99%"), (6, "100%")],
    )
    s3c = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%"), (1, "1%-20%"), (2, "21%-40%"), (3, "41%-60%"), (4, "61%-80%"),(5, "81%-99%"), (6, "100%")],
    )
    s4c = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%"), (1, "1%-20%"), (2, "21%-40%"), (3, "41%-60%"), (4, "61%-80%"),(5, "81%-99%"), (6, "100%")],
    )
    s5c = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%"), (1, "1%-20%"), (2, "21%-40%"), (3, "41%-60%"), (4, "61%-80%"),(5, "81%-99%"), (6, "100%")],
    )
    s1d = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%"), (1, "1%-20%"), (2, "21%-40%"), (3, "41%-60%"), (4, "61%-80%"),(5, "81%-99%"), (6, "100%")],
    )
    s2d = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%"), (1, "1%-20%"), (2, "21%-40%"), (3, "41%-60%"), (4, "61%-80%"),(5, "81%-99%"), (6, "100%")],
    )
    s3d = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%"), (1, "1%-20%"), (2, "21%-40%"), (3, "41%-60%"), (4, "61%-80%"),(5, "81%-99%"), (6, "100%")],
    )
    s4d = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%"), (1, "1%-20%"), (2, "21%-40%"), (3, "41%-60%"), (4, "61%-80%"),(5, "81%-99%"), (6, "100%")],
    )
    s5d = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%"), (1, "1%-20%"), (2, "21%-40%"), (3, "41%-60%"), (4, "61%-80%"),(5, "81%-99%"), (6, "100%")],
    )


# PAGES
class First_Mover(Page):
    form_model = 'player'
    form_fields = ['f1', 'f2', 'f3', 'f4', 'f5']

class Second_Mover(Page):
    form_model = 'player'
    form_fields = ['s1c', 's2c', 's3c', 's4c', 's5c', 's1d', 's2d', 's3d', 's4d', 's5d']



page_sequence = [First_Mover, Second_Mover]