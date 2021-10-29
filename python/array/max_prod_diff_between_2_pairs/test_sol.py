
import pytest
from max_prod_diff_between_2_pairs import Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

def test_nums1_returns_34(sol: Solution):
    assert sol.max_product_difference([5, 6, 2, 7, 4,]) == 34

def test_nums2_returns_64(sol: Solution):
    assert sol.max_product_difference([4, 2, 5, 9, 7, 4, 8,]) == 64

def test_nums3_returns_52(sol: Solution):
    assert sol.max_product_difference([5, 9, 7, 4, 8,]) == 52
