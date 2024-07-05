from api.models import Player, Deal, Pairing, Score, Table, Game
from django.conf import settings
import sqlite3
from bridge_movements.movement_loader import MovementLoader
from bridge_tools.game import GameCreator
from django.db import transaction


class DatabaseManager:
    @staticmethod
    def reset_db() -> None:
        Player.objects.all().delete()
        Deal.objects.all().delete()
        Pairing.objects.all().delete()
        Score.objects.all().delete()
        Table.objects.all().delete()
        Game.objects.all().delete()
        settings.DATABASES.get("default").get("ENGINE")

        db_name = settings.DATABASES.get("default").get("NAME")
        con = sqlite3.connect(db_name)
        cursor = con.cursor()
        cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='api_player';")
        cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='api_deal';")
        cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='api_score';")
        cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='api_pairing';")
        cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='api_table';")
        cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='api_game';")
        con.commit()

    @staticmethod
    @transaction.atomic
    def create_game(game: GameCreator) -> None:
        players = DatabaseManager._create_players(game.movement, game.game)
        deals = DatabaseManager._create_deals(game.movement, game.game)
        DatabaseManager._create_all_scores_and_tables(game.movement, players, deals,
                                                      game.game)

    @staticmethod
    def _create_players(movement: MovementLoader, game: Game) -> list[Player]:
        players = [Player(name=f"Player: {i + 1}", game=game) for i in range(
            movement.n_players)]
        Player.objects.bulk_create(players)
        return players

    @staticmethod
    def _create_deals(movement: MovementLoader, game: Game) -> list[Deal]:
        deals_in_order = len(movement.deals_order)
        deals = [
            Deal(
                vul=movement.deals_order[i % deals_in_order][0],
                dealer=movement.deals_order[i % deals_in_order][1],
                deal_number=i+1,
                game=game
            )
            for i in
            range(movement.n_deals)
        ]
        Deal.objects.bulk_create(deals)
        return deals

    @staticmethod
    def _create_all_scores_and_tables(movement: MovementLoader, players: list[Player],
                           deals: list[Deal], game: Game) -> None:
        for table_name in movement.movement:
            table = Table(game=game, table_number=table_name, actual_round=0)
            table.save()
            player_list = [pl['players'] for pl in movement.movement[
                table_name]]
            deals_list = [pl['deals'] for pl in movement.movement[
                table_name]]
            n_items = range(1, len(deals_list) + 1)
            for (n_round, n_players, n_deals) in zip(n_items, player_list,
                                                     deals_list):
                pair = Pairing(
                    round_number=n_round,
                    table=table,
                    n=players[n_players[0] - 1],
                    s=players[n_players[1] - 1],
                    e=players[n_players[2] - 1],
                    w=players[n_players[3] - 1]
                )
                pair.save()
                scores = [
                    Score(
                        game=game,
                        deal=deals[deal - 1],
                        pairing=pair
                    )
                    for deal in n_deals
                ]
                Score.objects.bulk_create(scores)
