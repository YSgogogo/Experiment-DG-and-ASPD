from otree.api import *
import random
from collections import defaultdict

doc = """
ASPD
"""

class C(BaseConstants):
    NAME_IN_URL = 'ASPD'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 18
    payoff_R1 = [650,  650,  650,  650,  650,  650,  650,  650, 900]
    payoff_R2 = [650,  650,  650,  650,  650,  650,  600,  650, 900]
    payoff_S1 = [250,  250,  250,  250,  250,  250,  250,  50,  250]
    payoff_T2 = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 700, 1000]

    payoff_T1 = [1000, 1000, 1000, 1000, 1000, 700,700, 1000, 1000]
    payoff_S2 = [250,  250,  250,  250,  50,   50, 250,  250,  250]
    payoff_D1 = [300,  300,  600,  600,  300, 300, 300,  300,  300]
    payoff_D2 = [300,  600,  300,  600,  300, 300, 300,  300,  300]


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    task1_number = models.IntegerField()
    task2_number = models.IntegerField()
    selected_round = models.IntegerField()

class Player(BasePlayer):
    timeSpent = models.FloatField()
    num_failed_attempts = models.IntegerField(initial=0)
    failed_too_many = models.BooleanField(initial=False)
    quiz1 = models.IntegerField(
        label="If First Mover chose A, then Seconder Mover knows the choice and decides A. Then First Mover gets:",
        widget=widgets.RadioSelect,
        choices=[
            [0, '400 tokens'],
            [1, '150 tokens'],
            [2, '350 tokens'],
        ]
    )
    quiz2 = models.IntegerField(
        label="If First Mover chose B, then Seconder Mover knows the choice and decides B. Then Second Mover gets:",
        widget=widgets.RadioSelect,
        choices=[
            [0, '200 tokens'],
            [1, '320 tokens'],
            [2, '180 tokens'],
        ]
    )
    quiz3 = models.BooleanField(label="Does First Mover know the choice of Second Mover prior to taking her decision?")
    quiz4 = models.BooleanField(label="Does Second Mover know the choice of First Mover prior to taking her decision?")

    choice_1st =  models.BooleanField(
        choices=[
           [True, 'coop'],
           [False, 'defect'],
        ]
    )

    choice_2nd_coop =  models.BooleanField(
        choices=[
           [True, 'coop'],
           [False, 'defect'],
        ]
    )

    choice_2nd_defect =  models.BooleanField(
        choices=[
           [True, 'coop'],
           [False, 'defect'],
        ]
    )

    task1_number = models.IntegerField()
    task2_number = models.IntegerField()
    selected_round = models.IntegerField()

def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for g in subsession.get_groups():
            game_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            random.shuffle(game_numbers)
            k=0
            for i in range(9):
                g.in_round(i+1).task1_number = game_numbers[i]
                k=k+1
                for p in g.get_players():
                    p.in_round(i+1).task1_number = g.in_round(i+1).task1_number
            for i in range(9):
                g.in_round(i+10).task2_number = game_numbers[i]
                k=k+1
                for p in g.get_players():
                    p.in_round(i+10).task2_number = g.in_round(i+10).task2_number


        for g in subsession.get_groups():
            random_round = random.randint(1, 9)
            g.in_round(18).selected_round = random_round
            for p in g.get_players():
                p.in_round(18).selected_round = g.in_round(18).selected_round



class ASPD_GamePage_1st(Page):
    form_model = 'player'
    form_fields = ['choice_1st','timeSpent']
    timer_text = 'Time remaining:'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number <= 9

    @staticmethod
    def vars_for_template(player):
        task1_number = player.task1_number
        return dict(
            R1 = C.payoff_R1[task1_number],
            S1 = C.payoff_S1[task1_number],
            T1 = C.payoff_T1[task1_number],
            D1 = C.payoff_D1[task1_number],
            R2 = C.payoff_R2[task1_number],
            S2 = C.payoff_S2[task1_number],
            T2 = C.payoff_T2[task1_number],
            D2 = C.payoff_D2[task1_number]
            )

class ASPD_GamePage_2nd(Page):
    form_model = 'player'
    form_fields = ['choice_2nd_defect', 'choice_2nd_coop','timeSpent']
    timer_text = 'Time remaining:'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number >= 10

    @staticmethod
    def vars_for_template(player):
        task2_number = player.task2_number
        return dict(
            R1=C.payoff_R1[task2_number],
            S1=C.payoff_S1[task2_number],
            T1=C.payoff_T1[task2_number],
            D1=C.payoff_D1[task2_number],
            R2=C.payoff_R2[task2_number],
            S2=C.payoff_S2[task2_number],
            T2=C.payoff_T2[task2_number],
            D2=C.payoff_D2[task2_number]
            )

class ASPD_Instructions(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class ASPD_Comprehension_Test(Page):
    form_model = 'player'
    form_fields = ['quiz1', 'quiz2', 'quiz3', 'quiz4']

    @staticmethod
    def error_message(player: Player, values):
        solutions = {"quiz1": 2, "quiz2": 0, "quiz3": False, "quiz4": True}
        errors = {name: 'Wrong' for name in solutions if values[name] != solutions[name]}
        if errors:
            player.num_failed_attempts += 1
            if player.num_failed_attempts >= 100:
                player.failed_too_many = True
            else:
                return errors

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Failed(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.failed_too_many



class ResultsWaitPage1(WaitPage):
    wait_for_all_groups = True
    def is_displayed(player:Player):
        return player.round_number==C.NUM_ROUNDS

class ResultsWaitPage(WaitPage):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    @staticmethod
    def after_all_players_arrive(group: Group):
        selected_round = group.selected_round
        group_in_selected_round = group.in_round(selected_round)
        selected_payment = group_in_selected_round.task1_number
        player_lists = group.get_players()
        player_1 = player_lists[0]
        player_2 = player_lists[1]
        player_1_in_selected_round = player_1.in_round(selected_round)
        player_2_in_selected_round = player_2.in_round(selected_round+9)
        if player_1_in_selected_round.choice_1st:
            if player_2_in_selected_round.choice_2nd_coop:
                player_1.payoff = C.payoff_R1[selected_payment]
                player_2.payoff = C.payoff_R2[selected_payment]
            else:
                player_1.payoff = C.payoff_S1[selected_payment]
                player_2.payoff = C.payoff_T2[selected_payment]
        else:
            if player_2_in_selected_round.choice_2nd_defect:
                player_1.payoff = C.payoff_T1[selected_payment]
                player_2.payoff = C.payoff_S2[selected_payment]
            else:
                player_1.payoff = C.payoff_D1[selected_payment]
                player_2.payoff = C.payoff_D2[selected_payment]
        player_1.participant.vars[__name__] = [str(player_1.payoff), 'First Mover', str(selected_round)]
        player_2.participant.vars[__name__] = [str(player_2.payoff), 'Second Mover', str(selected_round+9)]


page_sequence = [ASPD_Instructions, ASPD_Comprehension_Test, ASPD_GamePage_1st, ASPD_GamePage_2nd, ResultsWaitPage1, ResultsWaitPage]