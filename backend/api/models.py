from django.db import models
from datetime import datetime
from users.models import User

GAME_TYPES = [
    ("IND", "Individual Tournament"),
    ("PAIR", "Pair Tournament")
]

SCORE_TYPES = [
    ("CROSS_IMP", "Imp Scorer"),
    ("MAX", "Max Scorer")
]

STATUS_TYPES = [
    ("IN_PROGRESS", "Game in progress"),
    ("COMPLETED", "Game was completed")
]


class Movement(models.Model):
    name = models.TextField(max_length=100)
    type = models.TextField(max_length=4, choices=GAME_TYPES)
    n_players = models.IntegerField()
    n_tables = models.IntegerField()
    n_rounds = models.IntegerField()
    path = models.TextField()


class Game(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="games")
    name = models.TextField(max_length=100)
    date = models.DateTimeField(default=datetime.now)
    movement = models.ForeignKey(Movement, on_delete=models.CASCADE,
                                 related_name="games")
    deals_in_round = models.IntegerField()
    scorer = models.TextField(max_length=10, choices=SCORE_TYPES)
    status = models.TextField(default="IN_PROGRESS", choices=STATUS_TYPES)


class Table(models.Model):
    table_number = models.IntegerField()
    #table_user = models.ForeignKey(User....)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="tables")
    actual_round = models.IntegerField()


class Player(models.Model):
    name = models.TextField(max_length=8)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="players")


class Deal(models.Model):
    vul = models.TextField(max_length=1)
    deal_number = models.IntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="deals")
    dealer = models.TextField(max_length=1)


class Pairing(models.Model):
    round_number = models.IntegerField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE,
                              related_name="table")
    n = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="n_pairings")
    s = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="s_pairings")
    e = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="e_pairings")
    w = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="w_pairings")


class Score(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="scores")
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE, related_name="scores")
    pairing = models.ForeignKey(Pairing, on_delete=models.CASCADE,
                                related_name="scores")
    contract = models.TextField(max_length=8, null=True, blank=True)
    by = models.TextField(max_length=1, null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    result = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=4)
