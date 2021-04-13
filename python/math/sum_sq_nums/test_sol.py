
import pytest
from sum_of_square_numbers import Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

def test_5_true(
        sol: Solution,
        ):
    assert sol.judge_square_sum(5) == True

def test_8_true(
        sol: Solution,
        ):
    assert sol.judge_square_sum(8) == True

def test_349_true(
        sol: Solution,
        ):
    assert sol.judge_square_sum(349) == True

def test_0_true(
        sol: Solution,
        ):
    assert sol.judge_square_sum(0) == True

def test_1_true(
        sol: Solution,
        ):
    assert sol.judge_square_sum(1) == True

def test_27_false(
        sol: Solution,
        ):
    assert sol.judge_square_sum(27) == False

def test_4_true(
        sol: Solution,
        ):
    assert sol.judge_square_sum(4) == True

def test_3_false(
        sol: Solution,
        ):
    assert sol.judge_square_sum(3) == False

def test_999999999_false(
        sol: Solution,
        ):
    assert sol.judge_square_sum(999999999) == False


