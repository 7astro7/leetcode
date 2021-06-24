            
import pytest
from subtract_the_product_and_sum import Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

def test_n234_returns_15(sol: Solution):
    assert sol.subtract_product_and_sum(234) == 15

def test_n4421_returns_21(sol: Solution):
    assert sol.subtract_product_and_sum(4421) == 21

def test_n383_returns_58(sol: Solution):
    assert sol.subtract_product_and_sum(383) == 58

def test_n1004_returns_neg5(sol: Solution):
    assert sol.subtract_product_and_sum(1004) == -5
