from otree.api import *
import random

doc = """
Belief_elicitation
"""

class C(BaseConstants):
    NAME_IN_URL = 'Belief_elicitation'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 6
    payoff_R1 = [850,  850,  850,  850,  1200, 850 ]
    payoff_R2 = [850,  850,  850,  850,  1200, 1200]
    payoff_S1 = [400,  400,  400,  400,  400 , 400 ]
    payoff_T2 = [1250, 1250, 1250, 900,  1250, 1250]

    payoff_T1 = [1250, 1250, 1250, 1250, 1250, 1250]
    payoff_S2 = [400,  400,  50,   400,  400 , 400]
    payoff_D1 = [450,  450,  450,  450,  450 , 450]
    payoff_D2 = [450,  800,  450,  450,  450 , 450]


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    task_number = models.IntegerField()

class Player(BasePlayer):
    timeSpent = models.FloatField()
    task_number = models.IntegerField()
    cc = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%-20%"), (1, "21%-40%"), (2, "41%-60%"), (3, "61%-80%"),(4, "81%-100%")],
    )
    dc = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%-20%"), (1, "21%-40%"), (2, "41%-60%"), (3, "61%-80%"),(4, "81%-100%")],
    )
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for g in subsession.get_groups():
            game_numbers = [0, 1, 2, 3, 4, 5]
            random.shuffle(game_numbers)
            k=0
            for i in range(6):
                g.in_round(i+1).task_number = game_numbers[i]
                k=k+1
                for p in g.get_players():
                    p.in_round(i+1).task_number = g.in_round(i+1).task_number


class BE_Instructions(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Beliefs(Page):
    form_model = 'player'
    form_fields = ['cc','dc', 'timeSpent']
    timer_text = 'Time remaining:'

    @staticmethod
    def vars_for_template(player):
        task_number = player.task_number
        return dict(
            R1 = C.payoff_R1[task_number],
            S1 = C.payoff_S1[task_number],
            T1 = C.payoff_T1[task_number],
            D1 = C.payoff_D1[task_number],
            R2 = C.payoff_R2[task_number],
            S2 = C.payoff_S2[task_number],
            T2 = C.payoff_T2[task_number],
            D2 = C.payoff_D2[task_number]
            )


page_sequence = [BE_Instructions, Beliefs]