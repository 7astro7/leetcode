
import pytest
from power_of_2 import Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

def test_1_returns_true(
        sol: Solution,
        ):
    assert sol.is_power_of_two(1) 

def test_63_returns_false(
        sol: Solution,
        ):
    assert sol.is_power_of_two(63) == False

def test_5_returns_false(
        sol: Solution,
        ):
    assert sol.is_power_of_two(5) == False

def test_6_returns_false(
        sol: Solution,
        ):
    assert sol.is_power_of_two(6) == False

@pytest.fixture
def powers_of_2_all_true(
        sol: Solution,
        ) -> bool:
    for i in range(-32, 33):
        if not sol.is_power_of_two(2 ** i):
            return False
    return True

def test_powers_of_2_returns_true(
        sol: Solution,
        powers_of_2_all_true: bool,
        ):
    assert powers_of_2_all_true

@pytest.fixture
def not_power_of_2_sample_all_false(
        sol: Solution,
        ) -> bool:
    for i in range(33):
        if sol.is_power_of_two(-2 ** i):
            return False
    return True

def test_not_power_of_2_sample_returns_false(
        sol: Solution,
        not_power_of_2_sample_all_false: bool,
        ):
    assert not_power_of_2_sample_all_false

