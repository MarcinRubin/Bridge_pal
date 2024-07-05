from bridge_movements.movement_loader import IndividualMovementLoader, \
    PairMovementLoader, MovementLoader
from api.models import Game

"""
Class is responsible for game creation. It collects all the necessary data and load
the chosen movement using the movement loader class. Then the DatabaseManager saves all
necessary information that are necessary for the whole game
"""


class GameCreator:
    def __init__(self, game_instance: Game):
        self._game_instance = game_instance
        self._movement_instance = game_instance.movement
        self._movement = self._load_movement()

    def _load_movement(self) -> MovementLoader:
        if self._movement_instance.type == "IND":
            return IndividualMovementLoader(
                self._movement_instance.path,
                self._game_instance.deals_in_round,
                self._movement_instance.n_players
            )
        return PairMovementLoader(
            self._movement_instance.path,
            self._game_instance.deals_in_round,
            self._movement_instance.n_players
        )

    @property
    def game(self):
        return self._game_instance

    @property
    def movement(self):
        return self._movement
