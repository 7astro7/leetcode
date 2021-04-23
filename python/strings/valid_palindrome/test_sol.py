
import pytest
from valid_palindrome import Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

def test_one_char_true(
        sol: Solution,
        ):
    assert sol.is_palindrome("Q") == True

def test_hannah_true(
        sol: Solution,
        ):
    assert sol.is_palindrome("Hannah") == True

def test_panama_canal_string_true(
        sol: Solution,
        ):
    s = "A man, a plan, a canal: Panama"
    assert sol.is_palindrome(s) == True

def test_matrix_false(
        sol: Solution,
        ):
   assert sol.is_palindrome("matrix") == False

def test_90509_true(
        sol: Solution,
        ):
   assert sol.is_palindrome("90509") == True

def test_madam_im_adam_true(
        sol: Solution,
        ):
   assert sol.is_palindrome("Madam I'm Adam") == True

def test_greek_thing_true(
        sol: Solution,
        ):
   assert sol.is_palindrome("ΝΙΨΟΝ ΑΝΟΜΗΜΑΤΑ ΜΗ ΜΟΝΑΝ ΟΨΙΝ") == True

def test_mr_owl_true(
        sol: Solution,
        ):
   assert sol.is_palindrome("Mr. Owl ate my metal worm") == True

def test_mr_bowl_false(
        sol: Solution,
        ):
   assert sol.is_palindrome("Mr. Bowl ate my metal worm") == False


