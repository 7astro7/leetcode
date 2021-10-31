
import pytest
from check_if_sentence_is_pangram import Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

def test_sentence1_true(sol: Solution):
    assert sol.check_if_pangram("thequickbrownfoxjumpsoverthelazydog")

def test_sentence2_false(sol: Solution):
    assert sol.check_if_pangram("leetcode") == False

def test_sentence3_false(sol: Solution):
    assert sol.check_if_pangram("abcdefghijklmnopqrstuvwxy") == False
    
def test_sentence4_false(sol: Solution):
    sent4 = "jwtucoucmdfwxxqnxzkaxoglszmfrcvjoiunqqausaxxaaijyqdqgvdnqcaihwilqkpivenpnekioyqujrdrovqrlxovcucjqzjsxmllfgndfprctxvxwlzjtciqxgsxfwhmuzqvlksyuztoetyjugmswfjtawwaqmwyxmvo"
    assert sol.check_if_pangram(sent4) == False

