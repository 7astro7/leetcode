
import pytest
from count_negative_numbers_in_matrix import Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

def test_grid_1(sol: Solution):
    grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    assert sol.count_negatives(grid) == 8

def test_grid_2(sol: Solution):
    grid = [[-1]]
    assert sol.count_negatives(grid) == 1

def test_grid_3(sol: Solution):
    grid = [[1]]
    assert sol.count_negatives(grid) == 0

def test_grid_4(sol: Solution):
    grid = [[3, 2], [1, 1]]
    assert sol.count_negatives(grid) == 0
