
import pytest
from find_center_of_star_graph import Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

@pytest.fixture
def edges1() -> list:
    return [[1, 2,], [2, 3,], [4, 2,],]

def test_edges1_returns_2(
        sol: Solution,
        edges1: list,
        ):
    assert sol.find_center(edges1) == 2

@pytest.fixture
def edges2() -> list:
    return [[1, 2,], [5, 1,], [1, 3,], [1, 4,],]

def test_edges2_returns_1(
        sol: Solution,
        edges2: list,
        ):
    assert sol.find_center(edges2) == 1

@pytest.fixture
def edges3() -> list:
    return [
            [27, 8,], 
            [12, 27,], 
            [27, 4,],
            [27, 83,], 
            [27, 41,], 
            [27, 26,], 
            [27, 99,], 
            ]

def test_edges3_returns_27(
        sol: Solution,
        edges3: list,
        ):
    assert sol.find_center(edges3) == 27
