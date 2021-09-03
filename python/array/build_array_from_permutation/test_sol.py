
import pytest
from build_array_from_permutation import Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

def test_nums1(sol: Solution):
    nums = [0, 2, 1, 5, 3, 4,] 
    assert sol.build_array(nums) == [0, 1, 2, 4, 5, 3,]

def test_nums2(sol: Solution):
    nums = [5, 0, 1, 2, 3, 4,]
    assert sol.build_array(nums) == [4, 5, 0, 1, 2, 3,]

def test_nums3(sol: Solution):
    nums = [0, 1, 2, 3, 4, 5,]
    assert sol.build_array(nums) == list(range(6))
