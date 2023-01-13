from otree.api import *
import random

doc = """
ASPD
"""


class C(BaseConstants):
    NAME_IN_URL = 'ASPD'
    PLAYERS_PER_GROUP = 2
    TASKS = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3', 'A4', 'B4', 'C4']
    NUM_ROUNDS = len(TASKS)
    payoff_1R1 = cu(40)
    payoff_1S1 = cu(20)
    payoff_1T1 = cu(60)
    payoff_1D1 = cu(25)
    payoff_1R2 = cu(40)
    payoff_1S2 = cu(20)
    payoff_1T2 = cu(50)
    payoff_1D2 = cu(25)

    payoff_2R1 = cu(40)
    payoff_2S1 = cu(20)
    payoff_2T1 = cu(60)
    payoff_2D1 = cu(25)
    payoff_2R2 = cu(40)
    payoff_2S2 = cu(30)
    payoff_2T2 = cu(50)
    payoff_2D2 = cu(25)

    payoff_3R1 = cu(40)
    payoff_3S1 = cu(20)
    payoff_3T1 = cu(60)
    payoff_3D1 = cu(30)
    payoff_3R2 = cu(40)
    payoff_3S2 = cu(20)
    payoff_3T2 = cu(50)
    payoff_3D2 = cu(35)

    payoff_4R1 = cu(40)
    payoff_4S1 = cu(20)
    payoff_4T1 = cu(60)
    payoff_4D1 = cu(35)
    payoff_4R2 = cu(40)
    payoff_4S2 = cu(20)
    payoff_4T2 = cu(50)
    payoff_4D2 = cu(35)


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

    payoff_one = models.CurrencyField()
    payoff_two = models.CurrencyField()
    payoff_three = models.CurrencyField()
    payoff_four = models.CurrencyField()


    top1 = models.BooleanField(
        label='Now you are the first mover: you move first, and another participant will make choose after observing your choice. Please choose either Top or Down!',
        choices=[
           [True, 'Top'],
           [False, 'Down'],
        ]
    )
    L_after_T1 = models.BooleanField(
        label='Now you are the second mover: another participant who is the first mover has selected Top. Please choose either Left or Right',
        choices=[
           [True, 'Left'],
           [False, 'Right'],
        ]
    )
    L_after_D1 = models.BooleanField(
        label='Now you are the second mover: another participant who is the first mover has selected Down. Please choose either Left or Right',
        choices=[
           [True, 'Left'],
           [False, 'Right'],
        ]
    )


    top2 = models.BooleanField(
        label='Now you are the first mover: you move first, and another participant will make choose after observing your choice. Please choose either Top or Down!',
        choices=[
           [True, 'Top'],
           [False, 'Down'],
        ]
    )
    L_after_T2 = models.BooleanField(
        label='Now you are the second mover: another participant who is the first mover has selected Top. Please choose either Left or Right',
        choices=[
           [True, 'Left'],
           [False, 'Right'],
        ]
    )
    L_after_D2 = models.BooleanField(
        label='Now you are the second mover: another participant who is the first mover has selected Down. Please choose either Left or Right',
        choices=[
           [True, 'Left'],
           [False, 'Right'],
        ]
    )

    top3 = models.BooleanField(
        label='Now you are the first mover: you move first, and another participant will make choose after observing your choice. Please choose either Top or Down!',
        choices=[
           [True, 'Top'],
           [False, 'Down'],
        ]
    )
    L_after_T3 = models.BooleanField(
        label='Now you are the second mover: another participant who is the first mover has selected Top. Please choose either Left or Right',
        choices=[
           [True, 'Left'],
           [False, 'Right'],
        ]
    )
    L_after_D3 = models.BooleanField(
        label='Now you are the second mover: another participant who is the first mover has selected Down. Please choose either Left or Right',
        choices=[
           [True, 'Left'],
           [False, 'Right'],
        ]
    )


    top4 = models.BooleanField(
        label='Now you are the first mover: you move first, and another participant will make choose after observing your choice. Please choose either Top or Down!',
        choices=[
           [True, 'Top'],
           [False, 'Down'],
        ]
    )
    L_after_T4 = models.BooleanField(
        label='Now you are the second mover: another participant who is the first mover has selected Top. Please choose either Left or Right',
        choices=[
           [True, 'Left'],
           [False, 'Right'],
        ]
    )
    L_after_D4 = models.BooleanField(
        label='Now you are the second mover: another participant who is the first mover has selected Down. Please choose either Left or Right',
        choices=[
           [True, 'Left'],
           [False, 'Right'],
        ]
    )

def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            round_numbers = list(range(1, C.NUM_ROUNDS + 1))
            random.shuffle(round_numbers)
            task_rounds = dict(zip(C.TASKS, round_numbers))
            p.participant.task_rounds = task_rounds


class Instruction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class test(Page):
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

class ASPD1_1(Page):
    form_model = 'player'
    form_fields = ['top1']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['A1']

class ASPD1_2(Page):
    form_model = 'player'
    form_fields = ['L_after_T1']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['B1']

class ASPD1_3(Page):
    form_model = 'player'
    form_fields = ['L_after_D1']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['C1']

class ASPD2_1(Page):
    form_model = 'player'
    form_fields = ['top2']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['A2']

class ASPD2_2(Page):
    form_model = 'player'
    form_fields = ['L_after_T2']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['B2']

class ASPD2_3(Page):
    form_model = 'player'
    form_fields = ['L_after_D2']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['C2']

class ASPD3_1(Page):
    form_model = 'player'
    form_fields = ['top3']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['A3']

class ASPD3_2(Page):
    form_model = 'player'
    form_fields = ['L_after_T3']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['B3']

class ASPD3_3(Page):
    form_model = 'player'
    form_fields = ['L_after_D3']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['C3']

class ASPD4_1(Page):
    form_model = 'player'
    form_fields = ['top4']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['A4']

class ASPD4_2(Page):
    form_model = 'player'
    form_fields = ['L_after_T4']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['B4']

class ASPD4_3(Page):
    form_model = 'player'
    form_fields = ['L_after_D4']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['C4']


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






page_sequence = [Instruction, test, ASPD1_1, ASPD1_2, ASPD1_3, ASPD2_1, ASPD2_2, ASPD2_3, ASPD3_1, ASPD3_2, ASPD3_3, ASPD4_1, ASPD4_2, ASPD4_3, ResultsWaitPage, Results]
