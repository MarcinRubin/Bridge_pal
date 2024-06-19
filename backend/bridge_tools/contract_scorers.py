"""
Module responsible for a single contract scoring. It gets Parser object as an input
and returns the dictionary with the results needed for update
"""

from bridge_tools.parsers import ContractParser

SCORES = {
    "C": [0, 20, 40, 60, 80, 100, 120, 140],
    "D": [0, 20, 40, 60, 80, 100, 120, 140],
    "H": [0, 30, 60, 90, 120, 150, 180, 210],
    "S": [0, 30, 60, 90, 120, 150, 180, 210],
    "NT": [0, 40, 70, 100, 130, 160, 190, 220]
}

EXTRA = {
    "C": 20,
    "D": 20,
    "H": 30,
    "S": 30,
    "NT": 30,
    "X": 100,
    "XX": 200,
    "BASE": 0
}

LOSERS = {
    "normal": {
        "BASE": [0, 50, 100, 150, 200, 250, 300, 350],
        "X": [0, 100, 300, 500, 800, 1100, 1400, 1700],
        "XX": [0, 200, 600, 1000, 1600, 2200, 2800, 3200]
    },
    "vul": {
        "BASE": [0, 100, 200, 300, 400, 500, 600, 700],
        "X": [0, 200, 500, 800, 1100, 1400, 1700, 2000],
        "XX": [0, 400, 1000, 1600, 2200, 2800, 3400, 4000]
    }
}


class SingleDealScorer:
    @classmethod
    def get_result(cls, contract: ContractParser):
        if contract.is_won:
            return cls._handle_won(contract)
        return cls._handle_lost(contract)

    @staticmethod
    def _handle_won(contract: ContractParser) -> dict[str: int]:
        score = SCORES.get(contract.suit)[contract.level]

        if contract.double == "X":
            score *= 2
        elif contract.double == "XX":
            score *= 4

        if score < 100:
            score += 50
        else:
            if contract.vulnerability:
                score += 500
            else:
                score += 300

        if contract.level == 6:
            score += 750 if contract.vulnerability else 500
        if contract.level == 7:
            score += 1500 if contract.vulnerability else 1000

        if contract.double in {"X", "XX"}:
            vul_multiplier = 2 if contract.vulnerability else 1
            score += vul_multiplier * EXTRA[
                contract.double] * contract.extra
            score += 50 if contract.double == "X" else 100
        else:
            score += EXTRA[contract.suit] * contract.extra

        if contract.by in {"N", "S"}:
            return {"score": score}
        return {"score": -score}

    @staticmethod
    def _handle_lost(contract: ContractParser):
        vul_status = "vul" if contract.vulnerability else "normal"
        losers = contract.extra
        score = LOSERS.get(vul_status).get(contract.double)[losers]

        if contract.by in {"N", "S"}:
            return {"score": -score}
        return {"score": score}
