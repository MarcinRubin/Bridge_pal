from abc import ABC, abstractmethod

DEAL_ORDER = [["A", "N"], ["N", "E"], ["E", "S"], ["B", "W"],
              ["N", "N"], ["E", "E"], ["B", "S"], ["A", "W"],
              ["E", "N"], ["B", "E"], ["A", "S"], ["N", "W"],
              ["B", "N"], ["A", "E"], ["N", "S"], ["E", "W"]
              ]


class MovementLoader(ABC):
    def __init__(self, movement_path: str, deals_in_rounds: int, n_players: int):
        self._deals_in_round = int(deals_in_rounds)
        self._n_players = n_players
        self._deals_order = DEAL_ORDER
        self._movement = self._load_from_file(movement_path)
        self._rounds = self._get_rounds_number()
        self._n_deals = self._rounds * self._deals_in_round

    @abstractmethod
    def _load_from_file(self, path: str) -> dict:
        pass

    def _get_rounds_number(self):
        return len(list(self._movement.values())[0])

    @property
    def movement(self):
        return self._movement

    @property
    def n_players(self) -> int:
        return self._n_players

    @property
    def n_deals_in_round(self) -> int:
        return self._deals_in_round

    @property
    def deals_order(self):
        return self._deals_order

    @property
    def n_rounds(self) -> int:
        return self._rounds

    @property
    def n_deals(self) -> int:
        return self._n_deals

    @property
    def tables(self):
        return self._movement.keys()


class IndividualMovementLoader(MovementLoader):
    def _load_from_file(self, path: str):
        result = {}
        table_name = ""
        with open(path, "r") as file:
            for line in file:
                if line[0] in {"#", "\n"}:
                    continue
                if line[0] == "!":
                    table_name = line[1:].replace("\n", "")
                    result.update({table_name: []})
                    continue
                *players, deal_series = [int(i.replace("\n", "")) for i in
                                         line.split(" ")]
                deals = [(deal_series - 1) * self._deals_in_round + i for i in range(
                    1, self._deals_in_round + 1)]

                result.update(
                    {table_name: [*result.get(table_name), {"players": players,
                                                            "deals": deals}]})
        return result


class PairMovementLoader(MovementLoader):
    def _load_from_file(self, path: str):
        pass
