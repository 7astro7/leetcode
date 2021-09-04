
import pytest
from xor_operation_in_an_array import Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

def test_n_5_start_0(sol: Solution):
    assert sol.xor_operation(5, 0) == 8

def test_n_4_start_3(sol: Solution):
    assert sol.xor_operation(4, 3) == 8

def test_n_1_start_7(sol: Solution):
    assert sol.xor_operation(1, 7) == 7

def test_n_4_start_7(sol: Solution):
    assert sol.xor_operation(4, 7) == 8
