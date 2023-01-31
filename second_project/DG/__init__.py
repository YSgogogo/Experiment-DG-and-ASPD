import random
from otree.api import *
from collections import defaultdict

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
    quiz1 = models.IntegerField(label='If you are the First Mover, and you chose A. Then you get:')
    quiz2 = models.IntegerField(label='If you are the First Mover, and you chose B. Then you get:')
    quiz3 = models.IntegerField(label='If you are the First Mover, and you chose A. Then the Second Mover gets:')
    quiz4 = models.IntegerField(label='If you are the First Mover, and you chose B. Then the Second Mover gets:')
    quiz5 = models.IntegerField(label='If you are the Second Mover, and the First Mover chose A. Then you get:')
    quiz6 = models.IntegerField(label='If you are the Second Mover, and the First Mover chose B. Then you get:')
    quiz7 = models.IntegerField(label='If you are the Second Mover, and the First Mover chose A. Then the First Mover gets:')
    quiz8 = models.IntegerField(label='If you are the Second Mover, and the First Mover chose B. Then the First Mover gets:')
    quiz9 = models.BooleanField(label="Can the Second Mover decide the the final Points?")
    quiz10 = models.BooleanField(label="Can the First Mover decide the the final Points?")

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
    #creat a var to store the outcomes
    roles = models.StringField()
    #creat a var to store the roles

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

        if player.id_in_group == 1:
            player.roles = 'first mover'
        else:
            player.roles = 'second mover'


        random_round = random.randint(1, C.NUM_ROUNDS)
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
        solutions = dict(quiz1=40, quiz2=50, quiz3=45, quiz4=20, quiz5=45, quiz6=20, quiz7=40, quiz8=50, quiz9=False, quiz10=True)
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
    def is_displayed(player:Player):
        return player.round_number==C.NUM_ROUNDS
    def after_all_players_arrive(self):
        group_players = defaultdict(list)
        for p in self.subsession.get_players():
            group_players[p.group_id].append(p)
        for group_id, players in group_players.items():
            for p in players:
                selected_round = p.participant.selected_round
                player_in_selected_round = p.in_round(selected_round)
                selected_payment = player_in_selected_round.task_number
                player_lists = p.group.get_players()
                player_1 = player_lists[0]
                player_2 = player_lists[1]
                player_1_in_selected_round = player_1.in_round(selected_round)
                if player_1_in_selected_round.choice:
                    player_1.payoff = C.payoff_L1[selected_payment]
                    player_2.payoff = C.payoff_L2[selected_payment]
                else:
                    player_1.payoff = C.payoff_R1[selected_payment]
                    player_2.payoff = C.payoff_R2[selected_payment]
                player_1.participant.vars[__name__] = [str(player_1.payoff), 'First mover', str(selected_round)]
                player_2.participant.vars[__name__] = [str(player_2.payoff), 'Second mover', str(selected_round)]


    # show only in the final round
    # compute the payment for a random round selected for payment




page_sequence = [Main_Instructions, DG_Instructions, DG_Comprehension_Test, DG_GamePage, ResultsWaitPage]

