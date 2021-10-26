
import pytest
from three_divisors import Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

def test_n2_false(sol: Solution):
    assert sol.is_three(2) == False

def test_n4_true(sol: Solution):
    assert sol.is_three(4)

def test_n8_false(sol: Solution):
    assert sol.is_three(8) == False
    
def test_n9_true(sol: Solution):
    assert sol.is_three(9) 

def test_n25_true(sol: Solution):
    assert sol.is_three(25) 
