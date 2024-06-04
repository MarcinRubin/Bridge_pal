from bridge_movements.movement_loader import IndividualMovementLoader, \
    PairMovementLoader, MovementLoader
from bridge_tools.database_manager import DatabaseManager
from api.models import Game

"""
Class is responsible for game creation. It collects all the necessary data and load
the chosen movement using the movement loader class. Then the DatabaseManager saves all
necessary information that are necessary for the whole game
"""


class GameCreator:
    def __init__(self, game_instance: Game, movement_data: dict):
        self._game = game_instance
        self._movement_data = movement_data
        self._movement = self._load_movement()

    def _load_movement(self) -> MovementLoader:
        if self._movement_data.get("type") == "IND":
            return IndividualMovementLoader(
                self._movement_data.get("path"),
                self._game.deals_in_round,
                self._movement_data.get("players")
            )
        return PairMovementLoader(
            self._movement_data.get("path"),
            self._game.deals_in_round,
            self._movement_data.get("players")
        )

    def create(self) -> None:
        DatabaseManager.create_game(self._movement, self._game)

