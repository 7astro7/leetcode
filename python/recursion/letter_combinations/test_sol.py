
import pytest
import json
from letter_combinations import Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

@pytest.fixture
def two() -> list:
    return list('abc')

@pytest.fixture
def three() -> list:
    return list('def')

@pytest.fixture
def four() -> list:
    return list('ghi')

@pytest.fixture
def five() -> list:
    return list('jkl')

@pytest.fixture
def seven() -> list:
    return list('prqs')

@pytest.fixture
def nine() -> list:
    return list('wxyz')

def test_None(
        sol: Solution,
        ):
    assert sol.letter_combinations(None) == []

def test_empty(
        sol: Solution,
        ):
    assert sol.letter_combinations("") == []

def test_2(
        sol: Solution,
        two: list,
        ):
    assert sol.letter_combinations("2") == two

def test_23(
        sol: Solution,
        two: list,
        three: list,
        ):
    expected = [
            'ad', 'ae', 'af', 
            'bd', 'be', 'bf', 
            'cd', 'ce', 'cf',
            ]
    assert sol.letter_combinations("23") == expected

def test_2345(
        sol: Solution,
        two: list,
        three: list,
        four: list,
        five: list,
        ):
    with open('e2345.txt') as f:
        expected_map = json.load(f)
    expected = expected_map["2345"]
    assert sol.letter_combinations("2345") == expected

def test_79(
        sol: Solution,
        seven: list,
        nine: list,
        ):
    with open('e79.txt') as f:
        expected_map = json.load(f)
    expected = expected_map["79"]
    assert sol.letter_combinations("79") == expected

def test_234(
        sol: Solution,
        two: list,
        three: list,
        four: list,
        ):
    with open('e234.txt') as f:
        expected_map = json.load(f)
    expected = expected_map["234"]
    assert sol.letter_combinations("234") == expected


