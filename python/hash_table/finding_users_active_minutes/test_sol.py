
import pytest
from finding_active_minutes import Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

@pytest.fixture
def logs1() -> list:
    return [[0, 5,], [1, 2,], [0, 2,], [0, 5,], [1, 3,],]

def test_logs1_k5(
        sol: Solution,
        logs1: list,
        ):
    assert sol.uam(logs1, 5) == [0, 2,] + [0,] * 3

@pytest.fixture
def logs2() -> list:
    return [[1, 1,], [2, 2,], [2, 3,],]

def test_logs2_k4(
        sol: Solution,
        logs2: list,
        ):
    assert sol.uam(logs2, 4) == [1,] * 2 + [0,] * 2

@pytest.fixture
def logs3() -> list:
    return [[29, 1,], [29, 2,], [29, 3,], [6, 4,], 
            [8, 3,], [8, 5,], [29, 2,], [6, 4,],]

def test_logs3_k1(
        sol: Solution,
        logs3: list,
        ):
    assert sol.uam(logs3, 1) == [1,] 

def test_logs3_k2(
        sol: Solution,
        logs3: list,
        ):
    assert sol.uam(logs3, 2) == [1, 1,] 

def test_logs3_k3(
        sol: Solution,
        logs3: list,
        ):
    assert sol.uam(logs3, 3) == [1, 1, 1,] 










