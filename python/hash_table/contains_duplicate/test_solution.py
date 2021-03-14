
from contains_duplicate import Solution
import pytest

@pytest.fixture
def _1231():
    return list(range(1, 4)) + [1,]

@pytest.fixture
def _1234():
    return list(range(1, 5)) 

@pytest.fixture
def all_duplicate_list():
    return [1,] * 3 + [3,] * 2 + [4, 3, 2, 4, 2,]

@pytest.fixture
def ten_k_unique_list():
    return list(range(int(1e4)))

@pytest.fixture
def sol():
    return Solution()

def test_1_2_3_1_returns_true(sol: Solution, _1231):
    assert sol.contains_duplicate(_1231) == True

def test_1_2_3_4_returns_false(sol: Solution, _1234):
    assert sol.contains_duplicate(_1234) == False

def test_all_are_duplicate_returns_true(sol: Solution, 
        all_duplicate_list):
    assert sol.contains_duplicate(all_duplicate_list) == True

def test_10k_unique_returns_false(sol, ten_k_unique_list):
    assert sol.contains_duplicate(ten_k_unique_list) == False

