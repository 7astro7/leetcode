
import pytest
from decode_xored_array import Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

@pytest.fixture
def encoded1() -> list:
    return list(range(1, 4))

def test_encoded1_first1(
        sol: Solution,
        encoded1: list,
        ):
    assert sol.decode(encoded1, 1) == [1, 0, 2, 1,]

@pytest.fixture
def encoded2() -> list:
    return [6, 2, 7, 3,]

def test_encoded2_first4(
        sol: Solution,
        encoded2: list,
        ):
    assert sol.decode(encoded2, 4) == [4, 2, 0, 7, 4,]

def test_encoded2_first5(
        sol: Solution,
        encoded2: list,
        ):
    assert sol.decode(encoded2, 5) == [5, 3, 1, 6, 5,]

@pytest.fixture
def encoded3() -> list:
    return [641, 9, 71, 17,]

def test_encoded3_first5(
        sol: Solution,
        encoded3: list,
        ):
    assert sol.decode(encoded3, 5) == [5, 644, 653, 714, 731,]


