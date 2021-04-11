
import pytest
from valid_perfect_square import Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

@pytest.fixture
def squares_under_5k_all_true(
        sol: Solution,
        ) -> bool:
    for j in range(1, 5_001):
        if not sol.is_perfect_square(j ** 2):
            return False
    return True

def test_16_true(
        sol: Solution,
        ):
    assert sol.is_perfect_square(16) == True

def test_14_false(
        sol: Solution,
        ):
    assert sol.is_perfect_square(14) == False

def test_1_true(
        sol: Solution,
        ):
    assert sol.is_perfect_square(1) == True

def test_2_false(
        sol: Solution,
        ):
    assert sol.is_perfect_square(2) == False

def test_4_true(
        sol: Solution,
        ):
    assert sol.is_perfect_square(4) == True

def test_100_true(
        sol: Solution,
        ):
    assert sol.is_perfect_square(100) == True

def test_2401_true(
        sol: Solution,
        ):
    assert sol.is_perfect_square(2401) == True

def test_squares_to_5k_true(
        squares_under_5k_all_true: bool,
        ):
    assert squares_under_5k_all_true == True

