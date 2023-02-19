from otree.api import *
import random
from random import choice

doc = """
player's beliefs
"""

class C(BaseConstants):
    NAME_IN_URL = 'Belief_elicitation'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    num_failed_attempts = models.IntegerField(initial=0)
    failed_too_many = models.BooleanField(initial=False)

    o_choice = models.StringField()
    selected_question_number = models.IntegerField()
    paid_question = models.FloatField()

    f1 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%"), (1, "1%-20%"), (2, "21%-40%"), (3, "41%-60%"), (4, "61%-80%"),(5, "81%-99%"), (6, "100%")],
    )
    f2 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%"), (1, "1%-20%"), (2, "21%-40%"), (3, "41%-60%"), (4, "61%-80%"),(5, "81%-99%"), (6, "100%")],
    )
    f3 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%"), (1, "1%-20%"), (2, "21%-40%"), (3, "41%-60%"), (4, "61%-80%"),(5, "81%-99%"), (6, "100%")],
    )
    f4 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%"), (1, "1%-20%"), (2, "21%-40%"), (3, "41%-60%"), (4, "61%-80%"),(5, "81%-99%"), (6, "100%")],
    )
    f5 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%"), (1, "1%-20%"), (2, "21%-40%"), (3, "41%-60%"), (4, "61%-80%"),(5, "81%-99%"), (6, "100%")],
    )
    f6 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%"), (1, "1%-20%"), (2, "21%-40%"), (3, "41%-60%"), (4, "61%-80%"),(5, "81%-99%"), (6, "100%")],
    )
    f7 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%"), (1, "1%-20%"), (2, "21%-40%"), (3, "41%-60%"), (4, "61%-80%"),(5, "81%-99%"), (6, "100%")],
    )
    f8 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%"), (1, "1%-20%"), (2, "21%-40%"), (3, "41%-60%"), (4, "61%-80%"),(5, "81%-99%"), (6, "100%")],
    )
    f9 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%"), (1, "1%-20%"), (2, "21%-40%"), (3, "41%-60%"), (4, "61%-80%"),(5, "81%-99%"), (6, "100%")],
    )
    f10 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%"), (1, "1%-20%"), (2, "21%-40%"), (3, "41%-60%"), (4, "61%-80%"),(5, "81%-99%"), (6, "100%")],
    )
    f11 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%"), (1, "1%-20%"), (2, "21%-40%"), (3, "41%-60%"), (4, "61%-80%"),(5, "81%-99%"), (6, "100%")],
    )
    f12 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[(0, "0%"), (1, "1%-20%"), (2, "21%-40%"), (3, "41%-60%"), (4, "61%-80%"),(5, "81%-99%"), (6, "100%")],
    )


    quiz1 = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[
            [0, '£0'],
            [1, '£1.00'],
            [2, '£3.00'],
            [3, '£5.00'],
        ]
    )
    quiz2 = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[
            [0, '£0'],
            [1, '£1.00'],
            [2, '£3.00'],
            [3, '£5.00'],
        ]
    )
    quiz3 = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[
            [0, '£0.50'],
            [1, '£1.50'],
            [2, '£3.50'],
            [3, 'None of the options is correct'],
        ]
    )
    quiz4 = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[
            [0, 'Yes, they will'],
            [1, 'No, they will not'],
        ]
    )
    quiz5 = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[
            [0, 'Yes, they will'],
            [1, 'No, they will not'],
        ]
    )
    quiz6 = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[
            [0, 'Choose randomly'],
            [1, 'Simply state what I think'],
            [2, 'Always state one interval for all questions'],
        ]
    )

class Belief_elicitation_Instructions(Page):
    pass

class Belief_Comprehension_Test(Page):
    form_model = 'player'
    form_fields = ['quiz1', 'quiz2', 'quiz3', 'quiz4', 'quiz5', 'quiz6']

    @staticmethod
    def error_message(player: Player, values):
        solutions = dict(quiz1=0, quiz2=3, quiz3=3, quiz4=1, quiz5=0, quiz6=1)
        errors = {name: 'Wrong' for name in solutions if values[name] != solutions[name]}
        if errors:
            player.num_failed_attempts += 1
            if player.num_failed_attempts >= 100:
                player.failed_too_many = True
            else:
                return errors

class Failed(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.failed_too_many

class First_Mover(Page):
    form_model = 'player'
    form_fields = ['f1', 'f2', 'f3', 'f4']
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant

        if player.id_in_group == 1:
            options = [int(participant.vars['ASPD'][6]) + 1, int(participant.vars['ASPD'][6]) + 5,
                       int(participant.vars['ASPD'][6]) + 9]
            player.selected_question_number = choice(options)
            if player.selected_question_number == options[0]:
                player.o_choice = str(participant.vars['ASPD'][3])
                player.paid_question = player.selected_question_number
            elif player.selected_question_number == options[1]:
                player.o_choice = str(participant.vars['ASPD'][4])
                player.paid_question = player.selected_question_number + 0.1
            elif player.selected_question_number == options[2]:
                player.o_choice = str(participant.vars['ASPD'][5])
                player.paid_question = player.selected_question_number - 3.8

        else:
            options = [int(participant.vars['ASPD'][6]) + 1, int(participant.vars['ASPD'][6]) + 5,
                       int(participant.vars['ASPD'][6]) + 9]
            player.selected_question_number = choice(options)
            if player.selected_question_number == options[0]:
                player.o_choice = str(participant.vars['ASPD'][3])
                player.paid_question = player.selected_question_number
            elif player.selected_question_number == options[1]:
                player.o_choice = str(participant.vars['ASPD'][4])
                player.paid_question = player.selected_question_number + 0.1
            elif player.selected_question_number == options[2]:
                player.o_choice = str(participant.vars['ASPD'][5])
                player.paid_question = player.selected_question_number - 3.8

class Second_Mover(Page):
    form_model = 'player'
    form_fields = ['f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12']

class ResultsWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        player_lists = group.get_players()
        player_1 = player_lists[0]
        player_2 = player_lists[1]
        x = round(random.uniform(0, 1), 4)
        if getattr(player_1, "f" + str(player_1.selected_question_number)) == 0:
           if player_1.o_choice == str(True):
               if 1 < x:
                   player_1.payoff = 500
               else:
                   player_1.payoff = 0
           else:
               if 0 < x:
                   player_1.payoff = 500
               else:
                   player_1.payoff = 0

        elif getattr(player_1, "f" + str(player_1.selected_question_number)) == 1:
           if player_1.o_choice == str(True):
               if 0.64 < x:
                   player_1.payoff = 500
               else:
                   player_1.payoff = 0
           else:
               if 0.01 < x:
                   player_1.payoff = 500
               else:
                   player_1.payoff = 0

        elif getattr(player_1, "f" + str(player_1.selected_question_number)) == 2:
           if player_1.o_choice == str(True):
               if 0.36 < x:
                   player_1.payoff = 500
               else:
                   player_1.payoff = 0
           else:
               if 0.0421 < x:
                   player_1.payoff = 500
               else:
                   player_1.payoff = 0

        elif getattr(player_1, "f" + str(player_1.selected_question_number)) == 3:
           if player_1.o_choice == str(True):
               if 0.16 < x:
                   player_1.payoff = 500
               else:
                   player_1.payoff = 0
           else:
               if 0.1681 < x:
                   player_1.payoff = 500
               else:
                   player_1.payoff = 0

        elif getattr(player_1, "f" + str(player_1.selected_question_number)) == 4:
            if player_1.o_choice == str(True):
                if 0.04 < x:
                    player_1.payoff = 500
                else:
                    player_1.payoff = 0
            else:
                if 0.3721 < x:
                    player_1.payoff = 500
                else:
                    player_1.payoff = 0

        elif getattr(player_1, "f" + str(player_1.selected_question_number)) == 5:
            if player_1.o_choice == str(True):
                if 0.0001 < x:
                    player_1.payoff = 500
                else:
                    player_1.payoff = 0
            else:
                if 0.6561 < x:
                    player_1.payoff = 500
                else:
                    player_1.payoff = 0

        elif getattr(player_1, "f" + str(player_1.selected_question_number)) == 6:
            if player_1.o_choice == str(True):
                if 0 < x:
                    player_1.payoff = 500
                else:
                    player_1.payoff = 0
            else:
                if 1 < x:
                    player_1.payoff = 500
                else:
                    player_1.payoff = 0


        if getattr(player_2, "f" + str(player_2.selected_question_number)) == 0:
           if player_2.o_choice == str(True):
               if 1 < x:
                   player_2.payoff = 500
               else:
                   player_2.payoff = 0
           else:
               if 0 < x:
                   player_2.payoff = 500
               else:
                   player_2.payoff = 0

        elif getattr(player_2, "f" + str(player_2.selected_question_number)) == 1:
           if player_2.o_choice == str(True):
               if 0.64 < x:
                   player_2.payoff = 500
               else:
                   player_2.payoff = 0
           else:
               if 0.01 < x:
                   player_2.payoff = 500
               else:
                   player_2.payoff = 0

        elif getattr(player_2, "f" + str(player_2.selected_question_number)) == 2:
           if player_2.o_choice == str(True):
               if 0.36 < x:
                   player_2.payoff = 500
               else:
                   player_2.payoff = 0
           else:
               if 0.0421 < x:
                   player_2.payoff = 500
               else:
                   player_2.payoff = 0

        elif getattr(player_2, "f" + str(player_2.selected_question_number)) == 3:
           if player_2.o_choice == str(True):
               if 0.16 < x:
                   player_2.payoff = 500
               else:
                   player_2.payoff = 0
           else:
               if 0.1681 < x:
                   player_2.payoff = 500
               else:
                   player_2.payoff = 0

        elif getattr(player_2, "f" + str(player_2.selected_question_number)) == 4:
            if player_2.o_choice == str(True):
                if 0.04 < x:
                    player_2.payoff = 500
                else:
                    player_2.payoff = 0
            else:
                if 0.3721 < x:
                    player_2.payoff = 500
                else:
                    player_2.payoff = 0

        elif getattr(player_2, "f" + str(player_2.selected_question_number)) == 5:
            if player_2.o_choice == str(True):
                if 0.0001 < x:
                    player_2.payoff = 500
                else:
                    player_2.payoff = 0
            else:
                if 0.6561 < x:
                    player_2.payoff = 500
                else:
                    player_2.payoff = 0

        elif getattr(player_2, "f" + str(player_2.selected_question_number)) == 6:
            if player_2.o_choice == str(True):
                if 0 < x:
                    player_2.payoff = 500
                else:
                    player_2.payoff = 0
            else:
                if 1 < x:
                    player_2.payoff = 500
                else:
                    player_2.payoff = 0

        player_1.participant.vars[__name__] = [str(player_1.payoff), str(player_1.paid_question)]
        player_2.participant.vars[__name__] = [str(player_2.payoff), str(player_2.paid_question)]




page_sequence = [Belief_elicitation_Instructions, Belief_Comprehension_Test, First_Mover, Second_Mover, ResultsWaitPage]