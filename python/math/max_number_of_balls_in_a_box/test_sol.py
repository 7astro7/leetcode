
import pytest
from max_number_of_balls_in_a_box import Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

def test_lowlimit1_highlimit10_returns_2(sol: Solution):
    assert sol.count_balls(1, 10) == 2

def test_lowlimit5_highlimit15_returns_2(sol: Solution):
    assert sol.count_balls(5, 15) == 2

def test_lowlimit19_highlimit28_returns_2(sol: Solution):
    assert sol.count_balls(19, 28) == 2

def test_lowlimit20_highlimit21_returns_1(sol: Solution):
    assert sol.count_balls(20, 21) == 1
