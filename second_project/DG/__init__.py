import random
from otree.api import *


doc = """
DG
"""


class C(BaseConstants):
    NAME_IN_URL = 'DG'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 5
    
    # colliding all variables into 4 arrays:
    payoff_L1 = [40, 50, 50, 50, 50]
    payoff_L2 = [40, 20, 20, 20, 20]
    payoff_R1 = [20, 25, 30, 30, 30]
    payoff_R2 = [50, 30, 30, 25, 35]
    # end of arrays definitions


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    task_number = models.IntegerField()


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

    # choice of the dictator game
    #choice = models.IntegerField(initial = 0)
    choice =  models.BooleanField(
        choices=[
           [True, 'Left'],
           [False, 'Right'],
        ]
    )
    # I changed to the Booleanfield as integerfield leads one choice 'left' can not be chosen



    # choice is coded as:
    # -1 == left (first)
    # 1 == right (second)

    # getting the game numbers stored:
    task_number = models.IntegerField()
    DG_outcome = models.IntegerField()
    #creat a var to store the outcomes

def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for g in subsession.get_groups():
            game_numbers = [0, 1, 2, 3, 4]
            random.shuffle(game_numbers)
            k=0
            for i in range(C.NUM_ROUNDS): 
                g.in_round(i+1).task_number = game_numbers[i]
                k=k+1
                for p in g.get_players():
                    p.in_round(i+1).task_number = g.in_round(i+1).task_number
#            round_numbers = list(range(1, C.NUM_ROUNDS + 1))
#            random.shuffle(round_numbers)
#            task_rounds = dict(zip(C.TASKS, round_numbers))
#            p.participant.task_rounds = task_rounds

class DG_GamePage(Page):
    form_model = 'player'
    form_fields = ['choice']

    @staticmethod
    def vars_for_template(player):
        task_number = player.task_number
        return dict(
            L1 = C.payoff_L1[task_number],
            L2 = C.payoff_L2[task_number],
            R1 = C.payoff_R1[task_number],
            R2 = C.payoff_R2[task_number]
            )
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        if player.round_number == C.NUM_ROUNDS:
            random_round = random.randint(1, C.NUM_ROUNDS)
            participant.selected_round = random_round
            player_in_selected_round = player.in_round(random_round)
            player.payoff = player_in_selected_round.DG_outcome
#   randomly choose one round as payoff
class Main_Instructions(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class DG_Instructions(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class DG_Comprehension_Test(Page):
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
    @staticmethod
    def after_all_players_arrive(group: Group):
        task_number = group.task_number
        player_lists = group.get_players()
        player_1 = player_lists[0]
        player_2 = player_lists[1]
        if player_1.choice:
            player_1.DG_outcome = C.payoff_L1[task_number]
            player_2.DG_outcome = C.payoff_L2[task_number]
        else:
            player_1.DG_outcome = C.payoff_R1[task_number]
            player_2.DG_outcome = C.payoff_R2[task_number]
class DG_Results(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS


page_sequence = [Main_Instructions, DG_Instructions, DG_Comprehension_Test, DG_GamePage, ResultsWaitPage, DG_Results]

