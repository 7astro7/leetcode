
import pytest
from shuffle_the_array import Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

def test_nums1(sol: Solution):
    nums1 = [2, 5, 1, 3, 4, 7,]
    expected = [2, 3, 5, 4, 1, 7,]
    assert sol.shuffle(nums1, 3) == expected

def test_nums2(sol: Solution):
    nums2 = [1, 2, 3, 4, 4, 3, 2, 1,]
    expected = [1, 4, 2, 3, 3, 2, 4, 1,]
    assert sol.shuffle(nums2, 4) == expected


def test_nums3(sol: Solution):
    nums3 = [1, 1, 2, 2,]
    expected = [1, 2, 1, 2,]
    assert sol.shuffle(nums3, 2) == expected

def test_nums4(sol: Solution):
    nums4 = [1, 1, 2, 2,]
    expected = [1, 2, 1, 2,]
    assert sol.shuffle(nums4, 2) == expected
