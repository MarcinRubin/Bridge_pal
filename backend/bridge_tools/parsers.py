"""
This module contains a single ContractParser class. Its sole purpose is to validate
the correctness of the provided contract and provide a simple interface giving the
access to every property that is needed to calculate the score.

Is valid method should be used to determine if contract is valid bridge contract.
Similarly to serializers, the additional parameter raise_exception will force the
is_valid method to throw exception and return the error via endpoint
"""

import re
from rest_framework.exceptions import APIException
from rest_framework import status
from django.utils.translation import gettext_lazy as _

VULNERABILITY = {
    "A": {
        "N": False,
        "S": False,
        "E": False,
        "W": False
    },
    "B": {
        "N": True,
        "S": True,
        "E": True,
        "W": True
    },
    "N": {
        "N": True,
        "S": True,
        "E": False,
        "W": False
    },
    "E": {
        "N": False,
        "S": False,
        "E": True,
        "W": True
    }
}

VULNERABILITY_STATES = ["A", "B", "N", "E"]

CONTRACT_NAME_WITHOUT_DOUBLE = "BASE"


class ParseError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Invalid contract or vulnerability')
    default_code = 'invalid'

    def __init__(self, contract: dict[str:str]):
        super().__init__()
        self.contract = contract
        if contract["error"] == "contract":
            self.detail = f"{contract['value']} is not a valid bridge contract!"
        if contract["error"] == "vulnerability":
            self.detail = f"{contract['value']} is not a valid vulnerability state!"


class ContractParser:
    def __init__(self, contract: str, vulnerability: str):
        self._contract = contract.upper()
        self._vulnerability = vulnerability
        self._parsed_contract = self._parse_contract()

    def _parse_contract(self):
        return re.match(
            "^([1-7])(C|D|H|S|NT)(X{0,2})(-[1-7]|\+[1-7]|=)(N|S|E|W)$",
            self._contract
        )

    def is_valid(self, raise_exception: bool = False) -> bool:
        if self._parsed_contract is None:
            if raise_exception:
                raise ParseError({"error": "contract", "value": self._contract})
            return False

        if self._vulnerability not in VULNERABILITY_STATES:
            if raise_exception:
                raise ParseError({"error": "vulnerability", "value":
                    self._vulnerability})
            return False

        return True

    @property
    def contract(self) -> str:
        return self._parsed_contract.group(1) + self._parsed_contract.group(
            2) + self._parsed_contract.group(3) + self._parsed_contract.group(4)

    @property
    def extra(self) -> int:
        return 0 if self._parsed_contract.group(4) == "=" else \
            int(self._parsed_contract.group(4)[1])

    @property
    def suit(self) -> str:
        return self._parsed_contract.group(2)

    @property
    def level(self) -> int:
        return int(self._parsed_contract.group(1))

    @property
    def by(self) -> str:
        return self._parsed_contract.group(5)

    @property
    def is_won(self) -> bool:
        if self._parsed_contract.group(4)[0] == "-":
            return False
        return True

    @property
    def double(self) -> str:
        if self._parsed_contract.group(3) == "":
            return CONTRACT_NAME_WITHOUT_DOUBLE
        return self._parsed_contract.group(3)

    @property
    def vulnerability(self) -> bool:
        return VULNERABILITY[self._vulnerability][self.by]
