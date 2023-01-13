import random
from otree.api import *


doc = """
DG
"""


class C(BaseConstants):
    NAME_IN_URL = 'DG'
    PLAYERS_PER_GROUP = 2
    TASKS = ['A', 'B', 'C', 'D', 'E']
    NUM_ROUNDS = len(TASKS)

    payoff_1L1 = cu(40)
    payoff_1L2 = cu(40)
    payoff_1R1 = cu(20)
    payoff_1R2 = cu(50)

    payoff_2L1 = cu(50)
    payoff_2L2 = cu(20)
    payoff_2R1 = cu(25)
    payoff_2R2 = cu(30)

    payoff_3L1 = cu(50)
    payoff_3L2 = cu(20)
    payoff_3R1 = cu(30)
    payoff_3R2 = cu(30)

    payoff_4L1 = cu(50)
    payoff_4L2 = cu(20)
    payoff_4R1 = cu(30)
    payoff_4R2 = cu(25)

    payoff_5L1 = cu(50)
    payoff_5L2 = cu(20)
    payoff_5R1 = cu(30)
    payoff_5R2 = cu(35)

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    num_failed_attempts = models.IntegerField(initial=0)
    failed_too_many = models.BooleanField(initial=False)
    quiz1 = models.IntegerField(label='If you are the Dictator and select Left, and your randomly paired participant is the receiver. Then you get:')
    quiz2 = models.IntegerField(label='If you are the Dictator and select Right, and your randomly paired participant is the receiver. Then you get:')
    quiz3 = models.IntegerField(label='If you are the Dictator and select Left, and your randomly paired participant is the receiver. Then he/she gets:')
    quiz4 = models.IntegerField(label='If you are the Dictator and select Right, and your randomly paired participant is the receiver. Then he/she gets:')
    quiz5 = models.IntegerField(label='If you are the receiver, and your randomly paired participant is the dictator and select Left. Then you get:')
    quiz6 = models.IntegerField(label='If you are the receiver, and your randomly paired participant is the dictator and select Right. Then you get:')
    quiz7 = models.IntegerField(label='If you are the receiver, and your randomly paired participant is the dictator and select Left. Then he/she gets:')
    quiz8 = models.IntegerField(label='If you are the receiver, and your randomly paired participant is the dictator and select Right. Then he/she gets:')
    quiz9 = models.BooleanField(label="Can the receiver decide the the final Points?")
    quiz10 = models.BooleanField(label="Can the dictator decide the the final Points?")


    payoff_one = models.CurrencyField()
    payoff_two = models.CurrencyField()
    payoff_three = models.CurrencyField()
    payoff_four = models.CurrencyField()
    payoff_five = models.CurrencyField()

    one = models.BooleanField(
        label='Which of the following allocation you will choose',
        choices=[
           [True, 'Left'],
           [False, 'Right'],
        ]
    )
    two = models.BooleanField(
        label='Which of the following allocation you will choose',
        choices=[
           [True, 'Left'],
           [False, 'Right'],
        ]
    )
    three = models.BooleanField(
        label='Which of the following allocation you will choose',
        choices=[
           [True, 'Left'],
           [False, 'Right'],
        ]
    )
    four = models.BooleanField(
        label='Which of the following allocation you will choose',
        choices=[
           [True, 'Left'],
           [False, 'Right'],
        ]
    )
    five = models.BooleanField(
        label='Which of the following allocation you will choose',
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


class game_1(Page):
    form_model = 'player'
    form_fields = ['one']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['A']

class game_2(Page):
    form_model = 'player'
    form_fields = ['two']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['B']

class game_3(Page):
    form_model = 'player'
    form_fields = ['three']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['C']

class game_4(Page):
    form_model = 'player'
    form_fields = ['four']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['D']

class game_5(Page):
    form_model = 'player'
    form_fields = ['five']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['E']

class Welcome(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Instruction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class test(Page):
    form_model = 'player'
    form_fields = ['quiz1', 'quiz2', 'quiz3', 'quiz4', 'quiz5', 'quiz6', 'quiz7', 'quiz8', 'quiz9', 'quiz10']

    @staticmethod
    def error_message(player: Player, values):

        solutions = dict(quiz1=40, quiz2=50, quiz3=40, quiz4=20, quiz5=40, quiz6=20, quiz7=40, quiz8=50, quiz9=False, quiz10=True)


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
        return player.round_number == 5

    @staticmethod
    def after_all_players_arrive(group: Group):
        player_lists = group.get_players()
        player_1 = player_lists[0]
        player_2 = player_lists[1]
        if player_1.one:
                player_1.payoff_one = C.payoff_1L1
                player_2.payoff_one = C.payoff_1L2
        else:
                player_1.payoff_one = C.payoff_1R1
                player_2.payoff_one = C.payoff_1R2

        if player_1.two:
                player_1.payoff_two = C.payoff_2L1
                player_2.payoff_two = C.payoff_2L2
        else:
                player_1.payoff_two = C.payoff_2R1
                player_2.payoff_two = C.payoff_2R2

        if player_1.three:
                player_1.payoff_three = C.payoff_3L1
                player_2.payoff_three = C.payoff_3L2
        else:
                player_1.payoff_three = C.payoff_3R1
                player_2.payoff_three = C.payoff_3R2

        if player_1.four:
                player_1.payoff_four = C.payoff_4L1
                player_2.payoff_four = C.payoff_4L2
        else:
                player_1.payoff_four = C.payoff_4R1
                player_2.payoff_four = C.payoff_4R2

        if player_1.five:
                player_1.payoff_five = C.payoff_5L1
                player_2.payoff_five = C.payoff_5L2
        else:
                player_1.payoff_five = C.payoff_5R1
                player_2.payoff_five = C.payoff_5R2



page_sequence = [Welcome, Instruction, test, game_1, game_2, game_3, game_4, game_5, ResultsWaitPage, Results]
