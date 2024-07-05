from django.db.models.signals import post_save
from django.dispatch import receiver
from api.models import Game
from api.serializers import MovementSerializer
from bridge_tools.game import GameCreator
from bridge_tools.database_manager import DatabaseManager


@receiver(post_save, sender=Game)
def create_game(sender, instance, **kwargs):
    new_game = GameCreator(instance)
    DatabaseManager.create_game(new_game)
