
import pytest
from remove_all_occurences_of_a_substring import Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

def test_s_daabcbaabcbc_part_abc_returns_dab(sol: Solution):
    assert sol.remove_occurences('daabcbaabcbc', 'abc') == 'dab'

def test_s_axxxxyyyyb_part_xy_returns_ab(sol: Solution):
    assert sol.remove_occurences('axxxxyyyyb', 'xy') == 'ab'

def test_s_azsd_part_x_returns_azsd(sol: Solution):
    assert sol.remove_occurences('azsd', 'x') == 'azsd'

def test_s_wwboiiww_part_boii_returns_wwww(sol: Solution):
    assert sol.remove_occurences('wwboiiww', 'boii') == 'wwww'


