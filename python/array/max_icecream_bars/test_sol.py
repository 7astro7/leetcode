
import pytest
from max_icecream import Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

@pytest.fixture
def costs1() -> list:
    return [1, 3, 2, 4, 1,]

def test_costs1_coins7_returns_4(
        sol: Solution,
        costs1: list,
        ):
    assert sol.max_icecream(costs1, 7) == 4

@pytest.fixture
def costs2() -> list:
    return [1, 6, 3, 1, 2, 5,]

def test_costs2_coins20_returns_6(
        sol: Solution,
        costs2: list,
        ):
    assert sol.max_icecream(costs2, 20) == 6

@pytest.fixture
def costs3() -> list:
    return list(range(11))

def test_costs3_coins28_returns_8(
        sol: Solution,
        costs3: list,
        ):
    assert sol.max_icecream(costs3, 28) == 8

@pytest.fixture
def costs4() -> list:
    return [2, 2, 4, 4, 4, 4, 6, 7, 8, 8]

def test_costs4_coins41_returns_9(
        sol: Solution,
        costs4: list,
        ):
    assert sol.max_icecream(costs4, 41) == 9

def test_costs4_coins4_returns_2(
        sol: Solution,
        costs4: list,
        ):
    assert sol.max_icecream(costs4, 4) == 2

def test_costs4_coins40_returns_8(
        sol: Solution,
        costs4: list,
        ):
    assert sol.max_icecream(costs4, 40) == 8



