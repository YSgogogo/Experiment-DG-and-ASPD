import random
from otree.api import *
from collections import defaultdict

doc = """
DG
"""

class C(BaseConstants):
    NAME_IN_URL = 'DG'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 10
    payoff_L1 = [400, 50, 50, 50, 50, 50, 50, 180, 180, 180]
    payoff_L2 = [350, 360, 360, 360, 600, 600, 600, 600, 600, 600]
    payoff_R1 = [500, 200, 200, 380, 200, 200, 380, 200, 200, 380,]
    payoff_R2 = [150, 160, 320, 320, 160, 320, 320, 160, 320, 320,]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    task_number = models.IntegerField()
    selected_round = models.IntegerField()

class Player(BasePlayer):
    num_failed_attempts = models.IntegerField(initial=0)
    failed_too_many = models.BooleanField(initial=False)
    quiz1 = models.IntegerField(label='If First Mover chose A, then she gets:')
    quiz2 = models.IntegerField(label='If First Mover chose B, then she gets:')
    quiz3 = models.IntegerField(label='If First Mover chose A, then Second Mover gets:')
    quiz4 = models.IntegerField(label='If First Mover chose B, then Second Mover gets:')
    quiz5 = models.BooleanField(
        label="Who is able to decide the final points?",
        choices = [
            [True, 'First Mover'],
            [False, 'Second Mover'],
        ]
    )

    choice =  models.BooleanField(
        choices=[
           [True, 'Left'],
           [False, 'Right'],
        ]
    )

    task_number = models.IntegerField()
    selected_round = models.IntegerField()

def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for g in subsession.get_groups():
            game_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            random.shuffle(game_numbers)
            k=0
            for i in range(C.NUM_ROUNDS): 
                g.in_round(i+1).task_number = game_numbers[i]
                k=k+1
                for p in g.get_players():
                    p.in_round(i+1).task_number = g.in_round(i+1).task_number

        for g in subsession.get_groups():
            random_round = random.randint(1, C.NUM_ROUNDS)
            g.in_round(10).selected_round = random_round
            for p in g.get_players():
                p.in_round(10).selected_round = g.in_round(10).selected_round

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

class Main_Instructions(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class DG_Instructions(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Welcome(Page):
    def is_displayed(player:Player):
        return player.round_number==1

class DG_Comprehension_Test(Page):
    form_model = 'player'
    form_fields = ['quiz1', 'quiz2', 'quiz3', 'quiz4', 'quiz5']

    @staticmethod
    def error_message(player: Player, values):
        solutions = dict(quiz1=400, quiz2=500, quiz3=450, quiz4=200, quiz5=True)
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

class Wait(Page):
    def is_displayed(player:Player):
        return player.round_number==C.NUM_ROUNDS

class ResultsWaitPage(WaitPage):
    def is_displayed(player:Player):
        return player.round_number==C.NUM_ROUNDS
    @staticmethod
    def after_all_players_arrive(group: Group):
        selected_round = group.selected_round
        group_in_selected_round = group.in_round(selected_round)
        selected_payment = group_in_selected_round.task_number
        player_lists = group.get_players()
        player_1 = player_lists[0]
        player_2 = player_lists[1]
        player_1_in_selected_round = player_1.in_round(selected_round)
        if player_1_in_selected_round.choice:
            player_1.payoff = C.payoff_L1[selected_payment]
            player_2.payoff = C.payoff_L2[selected_payment]
        else:
            player_1.payoff = C.payoff_R1[selected_payment]
            player_2.payoff = C.payoff_R2[selected_payment]
        player_1.participant.vars[__name__] = [str(player_1.payoff), 'First Mover', str(selected_round)]
        player_2.participant.vars[__name__] = [str(player_2.payoff), 'Second Mover', str(selected_round)]




page_sequence = [Welcome, Main_Instructions, DG_Instructions, DG_Comprehension_Test, DG_GamePage, ResultsWaitPage, Wait]

