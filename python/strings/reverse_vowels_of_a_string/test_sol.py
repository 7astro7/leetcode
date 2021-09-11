
import pytest
from reverse_vowels import Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

def test_hello(sol: Solution):
    assert sol.reverse_vowels("hello") == "holle"

def test_leetcode(sol: Solution):
    assert sol.reverse_vowels("leetcode") == "leotcede"

def test_banana(sol: Solution):
    assert sol.reverse_vowels("banana") == "banana"

