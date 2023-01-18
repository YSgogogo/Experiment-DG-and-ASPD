from otree.api import *
import random

doc = """
ASPD
"""


class C(BaseConstants):
    NAME_IN_URL = 'ASPD'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 4
    payoff_R1 = [40, 40, 40, 40]
    payoff_S1 = [20, 20, 20, 20]
    payoff_T1 = [60, 60, 60, 60]
    payoff_D1 = [25, 25, 30, 35]
    payoff_R2 = [40, 40, 40, 40]
    payoff_S2 = [20, 30, 20, 20]
    payoff_T2 = [50, 50, 50, 50]
    payoff_D2 = [25, 25, 35, 35]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    num_failed_attempts = models.IntegerField(initial=0)
    failed_too_many = models.BooleanField(initial=False)
    quiz1 = models.IntegerField(label='If the First Mover chooses Top, then the Seconder Mover observed the choice and decide Left. Then the First Mover gets:')
    quiz2 = models.IntegerField(label='If the First Mover chooses Top, then the Seconder Mover observed the choice and decide Left. Then the Second Mover gets:')
    quiz3 = models.IntegerField(label='If the First Mover chooses Top, then the Seconder Mover observed the choice and decide Right. Then the First Mover gets:')
    quiz4 = models.IntegerField(label='If the First Mover chooses Top, then the Seconder Mover observed the choice and decide Right. Then the Second Mover gets:')
    quiz5 = models.IntegerField(label='If the First Mover chooses Down, then the Seconder Mover observed the choice and decide Left. Then the First Mover gets:')
    quiz6 = models.IntegerField(label='If the First Mover chooses Down, then the Seconder Mover observed the choice and decide Left. Then the Second Mover gets:')
    quiz7 = models.IntegerField(label='If the First Mover chooses Down, then the Seconder Mover observed the choice and decide Right. Then the First Mover gets:')
    quiz8 = models.IntegerField(label='If the First Mover chooses Down, then the Seconder Mover observed the choice and decide Right. Then the Second Mover gets:')
    quiz9 = models.BooleanField(label="Can the First Mover observe the Second Mover's choice before making decisions?")
    quiz10 = models.BooleanField(label="Can the Second Mover observe the First Mover's choice before making decisions?")


    choice_1st =  models.BooleanField(
        choices=[
           [True, 'Top'],
           [False, 'Down'],
        ]
    )
    choice_2nd_Top =  models.BooleanField(
        choices=[
           [True, 'Left'],
           [False, 'Right'],
        ]
    )
    choice_2nd_Down =  models.BooleanField(
        choices=[
           [True, 'Left'],
           [False, 'Right'],
        ]
    )


    task_number = models.IntegerField()

def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            game_numbers = [0, 1, 2, 3, 4]
            random.shuffle(game_numbers)
            k=0
            for i in range(C.NUM_ROUNDS):
                p.in_round(i+1).task_number = game_numbers[i]
                k=k+1


class ASPD_GamePage_1st(Page):
    form_model = 'player'
    form_fields = ['choice_1st']

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


class ASPD_GamePage_2nd_Top(Page):
    form_model = 'player'
    form_fields = ['choice_2nd_Top']

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

class ASPD_GamePage_2nd_Down(Page):
    form_model = 'player'
    form_fields = ['choice_2nd_Down']

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

class ASPD_Instructions(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class ASPD_Comprehension_Test(Page):
    form_model = 'player'
    form_fields = ['quiz1', 'quiz2', 'quiz3', 'quiz4', 'quiz5', 'quiz6', 'quiz7', 'quiz8', 'quiz9', 'quiz10']

    @staticmethod
    def error_message(player: Player, values):

        solutions = dict(quiz1=40, quiz2=40, quiz3=20, quiz4=50, quiz5=60, quiz6=20, quiz7=25, quiz8=25, quiz9=False, quiz10=True)


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

class ResultsWaitPage(WaitPage):
    wait_for_all_groups = True


class Results(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 12

    @staticmethod
    def after_all_players_arrive(group: Group):
        player_lists = group.get_players()
        player_1 = player_lists[0]
        player_2 = player_lists[1]
        if player_1.top1:
            if player_2.L_after_T1:
                player_1.payoff_one = C.payoff_1R1
                player_2.payoff_one = C.ppayoff_1R2
            else:
                player_1.payoff_one = C.payoff_1S1
                player_2.payoff_one = C.payoff_1T2
        else:
            if player_2.L_after_D1:
                player_1.payoff_one = C.payoff_1T1
                player_2.payoff_one = C.payoff_1S2
            else:
                player_1.payoff_one = C.payoff_1D1
                player_2.payoff_one = C.payoff_1D2

        if player_1.top2:
            if player_2.L_after_T2:
                player_1.payoff_two = C.payoff_2R1
                player_2.payoff_two = C.ppayoff_2R2
            else:
                player_1.payoff_two = C.payoff_2S1
                player_2.payoff_two = C.payoff_2T2
        else:
            if player_2.L_after_D2:
                player_1.payoff_two = C.payoff_2T1
                player_2.payoff_two = C.payoff_2S2
            else:
                player_1.payoff_two = C.payoff_2D1
                player_2.payoff_two = C.payoff_2D2

        if player_1.top3:
            if player_2.L_after_T3:
                player_1.payoff_three = C.payoff_3R1
                player_2.payoff_three = C.ppayoff_3R2
            else:
                player_1.payoff_three = C.payoff_3S1
                player_2.payoff_three = C.payoff_3T2
        else:
            if player_2.L_after_D3:
                player_1.payoff_three = C.payoff_3T1
                player_2.payoff_three = C.payoff_3S2
            else:
                player_1.payoff_three = C.payoff_3D1
                player_2.payoff_three = C.payoff_3D2

        if player_1.top4:
            if player_2.L_after_T4:
                player_1.payoff_four = C.payoff_4R1
                player_2.payoff_four = C.ppayoff_4R2
            else:
                player_1.payoff_four = C.payoff_4S1
                player_2.payoff_four = C.payoff_4T2
        else:
            if player_2.L_after_D4:
                player_1.payoff_four = C.payoff_4T1
                player_2.payoff_four = C.payoff_4S2
            else:
                player_1.payoff_four = C.payoff_4D1
                player_2.payoff_four = C.payoff_4D2






page_sequence = [ASPD_Instructions, ASPD_Comprehension_Test, ASPD_GamePage_1st, ASPD_GamePage_2nd_Top, ASPD_GamePage_2nd_Down]