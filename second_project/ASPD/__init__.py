from otree.api import *
import random
from collections import defaultdict

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
    task_number = models.IntegerField()

class Player(BasePlayer):
    num_failed_attempts = models.IntegerField(initial=0)
    failed_too_many = models.BooleanField(initial=False)
    quiz1 = models.IntegerField(label='If the First Mover chose A, then the Seconder Mover observed the choice and decides A. Then the First Mover gets:')
    quiz2 = models.IntegerField(label='If the First Mover chose A, then the Seconder Mover observed the choice and decides A. Then the Second Mover gets:')
    quiz3 = models.IntegerField(label='If the First Mover chose A, then the Seconder Mover observed the choice and decides B. Then the First Mover gets:')
    quiz4 = models.IntegerField(label='If the First Mover chose A, then the Seconder Mover observed the choice and decides B. Then the Second Mover gets:')
    quiz5 = models.IntegerField(label='If the First Mover chose B, then the Seconder Mover observed the choice and decides A. Then the First Mover gets:')
    quiz6 = models.IntegerField(label='If the First Mover chose B, then the Seconder Mover observed the choice and decides A. Then the Second Mover gets:')
    quiz7 = models.IntegerField(label='If the First Mover chose B, then the Seconder Mover observed the choice and decides B. Then the First Mover gets:')
    quiz8 = models.IntegerField(label='If the First Mover chose B, then the Seconder Mover observed the choice and decides B. Then the Second Mover gets:')
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
    roles = models.StringField()
    #creat a var to store the roles

def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for g in subsession.get_groups():
            game_numbers = [0, 1, 2, 3]
            random.shuffle(game_numbers)
            k=0
            for i in range(C.NUM_ROUNDS):
                g.in_round(i+1).task_number = game_numbers[i]
                k=k+1
                for p in g.get_players():
                    p.in_round(i+1).task_number = g.in_round(i+1).task_number

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

class ASPD_GamePage_2nd(Page):
    form_model = 'player'
    form_fields = ['choice_2nd_Down', 'choice_2nd_Top']

    @staticmethod
    def vars_for_template(player):
        task_number = player.task_number
        return dict(
            R1=C.payoff_R1[task_number],
            S1=C.payoff_S1[task_number],
            T1=C.payoff_T1[task_number],
            D1=C.payoff_D1[task_number],
            R2=C.payoff_R2[task_number],
            S2=C.payoff_S2[task_number],
            T2=C.payoff_T2[task_number],
            D2=C.payoff_D2[task_number]
            )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        random_round = random.randint(1, C.NUM_ROUNDS)
        if player.id_in_group == 1:
            player.roles = 'first mover'
        else:
            player.roles = 'second mover'

        if player.round_number == C.NUM_ROUNDS:
            # Group players by their group
            group_players = defaultdict(list)
            for p in player.subsession.get_players():
                group_players[p.group_id].append(p)
            # Generate a random number for each group
            for group_id, players in group_players.items():
                # Assign the generated number to all players in the group
                for p in players:
                    p.participant.selected_round = random_round
                    player_in_selected_round = player.in_round(random_round)
                    selected_payment = player_in_selected_round.task_number
            player_lists = player.group.get_players()
            player_1 = player_lists[0]
            player_2 = player_lists[1]
            if player_1.choice_1st:
                if player_2.choice_2nd_Top:
                    player_1.payoff = C.payoff_R1[selected_payment]
                    player_2.payoffe = C.payoff_R2[selected_payment]
                else:
                    player_1.payoff = C.payoff_S1[selected_payment]
                    player_2.payoff = C.payoff_T2[selected_payment]
            else:
                if player_2.choice_2nd_Down:
                    player_1.payoff = C.payoff_T1[selected_payment]
                    player_2.payoff = C.payoff_S2[selected_payment]
                else:
                    player_1.payoff = C.payoff_D1[selected_payment]
                    player_2.payoff = C.payoff_D2[selected_payment]


class ASPD_Instructions(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class ASPD_Comprehension_Test(Page):
    form_model = 'player'
    form_fields = ['quiz1', 'quiz2', 'quiz3', 'quiz4', 'quiz5', 'quiz6', 'quiz7', 'quiz8', 'quiz9', 'quiz10']

    @staticmethod
    def error_message(player: Player, values):
        solutions = dict(quiz1=35, quiz2=40, quiz3=20, quiz4=50, quiz5=60, quiz6=20, quiz7=30, quiz8=25, quiz9=False, quiz10=True)
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
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

class ASPD_Results(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS




page_sequence = [ASPD_Instructions, ASPD_Comprehension_Test, ASPD_GamePage_1st, ASPD_GamePage_2nd, ResultsWaitPage, ASPD_Results]