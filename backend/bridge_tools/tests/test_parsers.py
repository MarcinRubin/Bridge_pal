import pytest
from bridge_tools.parsers import ContractParser, ParseError

CONTRACTS = [
    ("3NT=N", "3NT=", 3, "NT", "Base", 0, "N", True),
    ("5C-1S", "5C-1", 5, "C", "Base", 1, "S", False),
    ("2H+1N", "2H+1", 2, "H", "Base", 1, "N", True),
    ("4s-3N", "4S-3", 4, "S", "Base", 3, "N", False),
    ("1d+6e", "1D+6", 1, "D", "Base", 6, "E", True),
    ("4nt-2n", "4NT-2", 4, "NT", "Base", 2, "N", False),
    ("5nt+1e", "5NT+1", 5, "NT", "Base", 1, "E", True),
    ("4sx-1n", "4SX-1", 4, "S", "X", 1, "N", False),
    ("4hxx-3n", "4HXX-3", 4, "H", "XX", 3, "N", False),
    ("3ntxx-2e", "3NTXX-2", 3, "NT", "XX", 2, "E", False),
    ("4ntxx+2e", "4NTXX+2", 4, "NT", "XX", 2, "E", True),
    ("5dxx-2e", "5DXX-2", 5, "D", "XX", 2, "E", False),
    ("1cx=n", "1CX=", 1, "C", "X", 0, "N", True),
    ("2hx+2w", "2HX+2", 2, "H", "X", 2, "W", True)
]

INVALID_CONTRACTS = [
    "dcadaw", "3nt=g", "8d=n", "-1c-1n", "12h=e", "5b=n", "3ntxxx=n", "3nt n-1e"
]

VALID_VULNERABILITIES = ["A", "B", "N", "S"]


@pytest.mark.parametrize("contract", [i[0] for i in CONTRACTS])
def test_if_is_valid_returns_true_if_contract_is_valid(contract):
    parser = ContractParser(contract, "A")
    assert parser.is_valid()


@pytest.mark.parametrize("contract", INVALID_CONTRACTS)
@pytest.mark.parametrize("vulnerability", VALID_VULNERABILITIES)
def test_if_is_valid_returns_false_if_contract_is_invalid(contract, vulnerability):
    parser = ContractParser(contract, vulnerability)
    assert not parser.is_valid()


@pytest.mark.parametrize("contract", [i[0] for i in CONTRACTS])
@pytest.mark.parametrize("vulnerability", ["Z", "sdfsd", "S", "W", "123", ""])
def test_if_is_valid_returns_false_if_vulnerability_is_invalid(contract, vulnerability):
    print(contract, vulnerability)
    parser = ContractParser(contract, vulnerability)
    assert not parser.is_valid()


@pytest.mark.parametrize("contract", INVALID_CONTRACTS)
def test_if_is_valid_throw_error_if_the_raise_exception_is_equal_to_true(contract):
    parser = ContractParser(contract, "A")
    with pytest.raises(ParseError) as exc_info:
        parser.is_valid(raise_exception=True)
    assert str(exc_info.value) == f"{contract.upper()} is not a valid bridge contract!"

@pytest.mark.parametrize("contract", INVALID_CONTRACTS)
def test_if_is_valid_throw_error_if_the_raise_exception_is_equal_to_true_2(contract):
    parser = ContractParser(contract, "A")
    with pytest.raises(ParseError) as exc_info:
        parser.is_valid(raise_exception=True)
    assert str(exc_info.value) == f"{contract.upper()} is not a valid bridge contract!"


@pytest.mark.parametrize(("contract", "output"), [(i[0], i[1]) for i in CONTRACTS])
def test_if_method_contract_returns_a_valid_contract(contract, output):
    parser = ContractParser(contract, "A")
    assert parser.contract == output


@pytest.mark.parametrize(("contract", "output"), [(i[0], i[5]) for i in CONTRACTS])
def test_if_method_extra_returns_a_valid_number_of_over_and_under_tricks(contract,
                                                                         output):
    parser = ContractParser(contract, "A")
    assert parser.extra == output


@pytest.mark.parametrize(("contract", "output"), [(i[0], i[3]) for i in CONTRACTS])
def test_if_method_suit_returns_a_valid_suit(contract, output):
    parser = ContractParser(contract, "A")
    assert parser.suit == output


@pytest.mark.parametrize(("contract", "output"), [(i[0], i[2]) for i in CONTRACTS])
def test_if_method_suit_returns_a_valid_level(contract, output):
    parser = ContractParser(contract, "A")
    assert parser.level == output\


@pytest.mark.parametrize(("contract", "output"), [(i[0], i[6]) for i in CONTRACTS])
def test_if_method_suit_returns_a_valid_by(contract, output):
    parser = ContractParser(contract, "A")
    assert parser.by == output


@pytest.mark.parametrize(("contract", "output"), [(i[0], i[7]) for i in CONTRACTS])
def test_if_method_suit_returns_a_valid_is_won(contract, output):
    parser = ContractParser(contract, "A")
    assert parser.is_won == output


@pytest.mark.parametrize(("contract", "output"), [(i[0], i[4]) for i in CONTRACTS])
def test_if_method_suit_returns_a_valid_double_output(contract, output):
    parser = ContractParser(contract, "A")
    assert parser.double == output


@pytest.mark.parametrize(("contract", "output"), [(i[0], i[4]) for i in CONTRACTS])
def test_if_method_suit_returns_a_valid_result(contract, output):
    parser = ContractParser(contract, "A")
    assert parser.double == output


@pytest.mark.parametrize(("contract", "output"), [(i[0], i[4]) for i in CONTRACTS])
@pytest.mark.parametrize("vulnerability", ["A", "B", "N", "E"])
def test_if_method_suit_returns_correct_vulnerability(contract, output, vulnerability):
    parser = ContractParser(contract, vulnerability)
    assert parser.double == output