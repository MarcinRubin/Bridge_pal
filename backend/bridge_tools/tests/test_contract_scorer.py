import pytest
from bridge_tools.parsers import ContractParser
from bridge_tools.contract_scorers import SingleDealScorer


CONTRACTS = [
    ("3NT=N", "A"),
]

@pytest.mark.parametrize("contract"
def test_if_handle_won_method_returns_valid_results_objects(parser):
    result = SingleDealScorer._handle_won(parser)
    print(result)
    assert 1