from django.core.management.base import BaseCommand
from api.models import Movement
from bridge_movements.movements import MOVEMENTS


class Command(BaseCommand):
    help = "Load all movements specified in the bridge_movement/movement.py to DB"

    def handle(self, *args, **kwargs):
        self.stdout.write("Updating movement table...")
        for movement_data in MOVEMENTS:
            Movement.objects.get_or_create(**movement_data)
        self.stdout.write("Movements updated")
