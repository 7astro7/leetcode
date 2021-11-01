
import pytest
from replace_all_digits_with_characters import Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

def test_s1_returns_abcdef(sol: Solution):
    assert sol.replace_digits('a1c1e1') == 'abcdef'

def test_s2_returns_abbdcfdhe(sol: Solution):
    assert sol.replace_digits('a1b2c3d4e') == 'abbdcfdhe'

def test_s3_returns_bip(sol: Solution):
    assert sol.replace_digits('b7p') == 'bip'
