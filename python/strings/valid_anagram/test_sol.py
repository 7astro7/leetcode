
import pytest
from valid_anagram import Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

def test_anagram_nagaram_true(sol: Solution):
    assert sol.is_anagram("anagram", "nagaram")

def test_rat_car_false(sol: Solution):
    assert sol.is_anagram("rat", "car") == False

def test_listen_silent_true(sol: Solution):
    assert sol.is_anagram("listen", "silent")
