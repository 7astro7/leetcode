
import pytest
from counting_bits import Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

def test_n2_returns(sol: Solution):
    assert sol.count_bits(2) == [0, 1, 1,]

def test_n5_returns(sol: Solution):
    assert sol.count_bits(5) == [0, 1, 1, 2, 1, 2,]

def test_n7_returns(sol: Solution):
    assert sol.count_bits(7) == [0, 1, 1, 2, 1, 2, 2, 3,]
