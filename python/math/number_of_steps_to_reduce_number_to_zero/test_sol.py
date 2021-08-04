
import pytest
from number_of_steps_to_reduce import Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

def test_14_returns_6(sol: Solution):
    assert sol.number_of_steps(14) == 6

def test_8_returns_4(sol: Solution):
    assert sol.number_of_steps(8) == 4

def test_1_returns_1(sol: Solution):
    assert sol.number_of_steps(1) == 1

def test_0_returns_0(sol: Solution):
    assert sol.number_of_steps(0) == 0

def test_123_returns_12(sol: Solution):
    assert sol.number_of_steps(123) == 12
