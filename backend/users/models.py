from django.db import models
from api.models import Game, Table


class CoordinatorProfile:
    current_game = models.ForeignKey(Game, on_delete=models.SET_NULL)


class TableProfile:
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    round = models.IntegerField(default=0)
