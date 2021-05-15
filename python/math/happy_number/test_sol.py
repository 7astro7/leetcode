
import pytest
from happy_number import Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

def test_2_false(
        sol: Solution,
        ):
    assert sol.is_happy(2) == False

def test_10_true(
        sol: Solution,
        ):
    assert sol.is_happy(10) == True

def test_476_false(
        sol: Solution,
        ):
    assert sol.is_happy(476) == False

def test_19_true(
        sol: Solution,
        ):
    assert sol.is_happy(19) == True

def test_20_false(
        sol: Solution,
        ):
    assert sol.is_happy(20) == False

def test_111111_false(
        sol: Solution,
        ):
    assert sol.is_happy(111111) == False

def test_2121_true(
        sol: Solution,
        ):
    assert sol.is_happy(2121) == True


