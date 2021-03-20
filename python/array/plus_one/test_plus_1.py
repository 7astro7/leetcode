
import pytest
from plus_one import Solution

@pytest.fixture
def zero():
    return [0,]

@pytest.fixture
def _9():
    return [9,]

@pytest.fixture
def _123():
    return list(range(1, 4))

@pytest.fixture
def _9092():
    return [9, 0, 9, 2,]

@pytest.fixture
def _999():
    return [9, 9, 9,]

@pytest.fixture
def sol():
    return Solution()

def test_zero_returns_1(zero: list, sol: Solution):
    assert sol.plus_one(zero) == [1,]

def test_123_returns_124(_123: list, sol: Solution):
    assert sol.plus_one(_123) == [1, 2, 4,]

def test_9092_returns_9093(_9092: list, sol: Solution):
    assert sol.plus_one(_9092) == [9, 0, 9, 3,]

def test_9_returns_1e1(_9: list, sol: Solution):
    assert sol.plus_one(_9) == [1, 0,]

def test_999_returns_1e3(_999: list, sol: Solution):
    assert sol.plus_one(_999) == [1, 0, 0, 0,]
