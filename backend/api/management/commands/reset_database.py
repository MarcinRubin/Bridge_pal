from django.conf import settings
from django.core.management.base import BaseCommand
from api.models import Player, Deal, Pairing, Score, Table
import sqlite3

# For this moment edit this to set up new database for a given movement
DEALS_IN_ROUND = 3
N_PLAYERS = 12
FILENAME = "./movements/movement.txt"
#######################################################################


class Command(BaseCommand):
    help = "Setup the db for a game"

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.movement_loader = MovementLoader(FILENAME, DEALS_IN_ROUND, N_PLAYERS)

    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        Player.objects.all().delete()
        Deal.objects.all().delete()
        Pairing.objects.all().delete()
        Score.objects.all().delete()
        Table.objects.all().delete()
        self.stdout.write("Creating new data...")
        settings.DATABASES.get("default").get("ENGINE")

        db_name = settings.DATABASES.get("default").get("NAME")
        con = sqlite3.connect(db_name)
        cursor = con.cursor()
        cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='api_player';")
        cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='api_deal';")
        cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='api_score';")
        cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='api_pairing';")
        con.commit()

        #self._create_db()

    def _create_db(self):
        players = self._create_players()
        deals = self._create_deals()
        self._create_tables_and_scores(players, deals)

    def _create_players(self):
        players = [Player(name=f"Player: {i + 1}") for i in range(
            self.movement_loader.n_players)]
        Player.objects.bulk_create(players)
        return players

    def _create_deals(self):
        deals_in_order = len(self.movement_loader.deals_order)
        deals = [
            Deal(
                vul=self.movement_loader.deals_order[i % deals_in_order][0],
                dealer=self.movement_loader.deals_order[i % deals_in_order][1]
            )
            for i in
            range(self.movement_loader.n_deals)
        ]
        Deal.objects.bulk_create(deals)
        return deals

    def _create_tables_and_scores(self, players, deals):
        for table_name in self.movement_loader.movement:
            player_list = [pl['players'] for pl in self.movement_loader.movement[
                table_name]]
            deals_list = [pl['deals'] for pl in self.movement_loader.movement[
                table_name]]
            n_items = range(1, len(deals_list) + 1)
            for (n_round, n_players, n_deals) in zip(n_items, player_list, deals_list):
                pair = Pairing(
                    round_number=n_round,
                    table_name=table_name,
                    n=players[n_players[0] - 1],
                    s=players[n_players[1] - 1],
                    e=players[n_players[2] - 1],
                    w=players[n_players[3] - 1]
                )
                pair.save()
                scores = [
                    Score(
                        deal=deals[deal - 1],
                        pairing=pair
                    )
                    for deal in n_deals
                ]
                Score.objects.bulk_create(scores)

