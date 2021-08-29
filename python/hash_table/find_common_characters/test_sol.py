
import pytest
from find_common_characters import Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

def test_words1(sol: Solution):
    words = ["bella", "label", "roller"]
    assert sol.common_chars(words) == ["e", "l", "l",]

def test_words2(sol: Solution):
    words = ["cool", "lock", "cook",]
    assert sol.common_chars(words) == ["c", "o",]

def test_words3(sol: Solution):
    words = ["extend", "tend", "tender",]
    assert sorted(sol.common_chars(words)) == sorted(["t", "e", "n", "d",])

def test_words4(sol: Solution):
    words = ["timothy", "timbuktu", "timber", "timourous", "timid"]
    assert sorted(sol.common_chars(words)) == sorted(["i", "m", "t",])
