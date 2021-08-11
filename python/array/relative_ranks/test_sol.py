
import pytest
from relative_ranks import Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

def test_score1(sol: Solution):
    score1 = [5, 4, 3, 2, 1,]
    expected = ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5",]
    assert sol.find_relative_ranks(score1) == expected

def test_score2(sol: Solution):
    score2 = [10, 3, 8, 9, 4,]
    expected = ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4",]
    assert sol.find_relative_ranks(score2) == expected

def test_score3(sol: Solution):
    score3 = [200, 190, 54, 29, 300, 400,]
    expected = ["Bronze Medal", "4", "5", "6", "Silver Medal", "Gold Medal",]
    assert sol.find_relative_ranks(score3) == expected
