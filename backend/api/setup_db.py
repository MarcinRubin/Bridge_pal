from bridge_movements.movement_loader import MovementLoader
from django.conf import settings
import sqlite3
from .models import Player, Deal, Score, Pairing


class SetupDb:
    def __init__(self, movement: MovementLoader):
        self._movement = movement

    def exec(self):
        self._reset_db()
        self._create_db()

    def _reset_db(self):
        print("Deleting old data...")
        Player.objects.all().delete()
        Deal.objects.all().delete()
        Pairing.objects.all().delete()
        Score.objects.all().delete()
        print("Creating new data...")
        settings.DATABASES.get("default").get("ENGINE")

        db_name = settings.DATABASES.get("default").get("NAME")
        con = sqlite3.connect(db_name)
        cursor = con.cursor()
        cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='api_player';")
        cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='api_deal';")
        cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='api_score';")
        cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='api_pairing';")
        con.commit()

    def _create_db(self):
        players = self._create_players()
        deals = self._create_deals()
        self._create_tables_and_scores(players, deals)

    def _create_players(self):
        players = [Player(name=f"Player: {i + 1}") for i in range(
            self._movement.n_players)]
        Player.objects.bulk_create(players)
        return players

    def _create_deals(self):
        deals_in_order = len(self._movement.deals_order)
        deals = [
            Deal(
                vul=self._movement.deals_order[i % deals_in_order][0],
                dealer=self._movement.deals_order[i % deals_in_order][1]
            )
            for i in
            range(self._movement.n_deals)
        ]
        Deal.objects.bulk_create(deals)
        return deals

    def _create_tables_and_scores(self, players, deals):
        for table_name in self._movement.movement:
            player_list = [pl['players'] for pl in self._movement.movement[
                table_name]]
            deals_list = [pl['deals'] for pl in self._movement.movement[
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
