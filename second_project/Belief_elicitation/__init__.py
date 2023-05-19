from otree.api import *
import random

doc = """
Belief_elicitation
"""

class C(BaseConstants):
    NAME_IN_URL = 'Belief_elicitation'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 5
    payoff_R1 = [650,  650,  650,  650,  650 ]
    payoff_R2 = [650,  650,  650,  650,  650 ]
    payoff_S1 = [200,  200,  200,  200,  50  ]
    payoff_T2 = [900,  900,  900,  900,  750 ]

    payoff_T1 = [900,  900,  900,  900,  750 ]
    payoff_S2 = [200,  200,  200,  200,  50  ]
    payoff_D1 = [250,  250,  600,  600,  600 ]
    payoff_D2 = [250,  600,  250,  600,  600 ]


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
            game_numbers = [0, 1, 2, 3, 4]
            random.shuffle(game_numbers)
            k=0
            for i in range(5):
                g.in_round(i+1).task_number = game_numbers[i]
                k=k+1
                for p in g.get_players():
                    p.in_round(i+1).task_number = g.in_round(i+1).task_number


class BE_Instructions(Page):
    pass

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