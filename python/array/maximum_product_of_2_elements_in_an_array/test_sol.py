
import pytest
from max_product_of_2_elements import Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

def test_nums1_returns_12(sol: Solution):
    assert sol.max_product([3, 4, 5, 2,]) == 12

def test_nums2_returns_16(sol: Solution):
    assert sol.max_product([1, 5, 4, 5,]) == 16

def test_nums3_returns_12(sol: Solution):
    assert sol.max_product([3, 7,]) == 12

def test_nums4_returns_96(sol: Solution):
    assert sol.max_product([3, 7, 9, 13, 4, 2]) == 96
