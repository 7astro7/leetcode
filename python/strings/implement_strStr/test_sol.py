
import pytest
from implement_strstr import Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

def test_ll_hello_returns_2(
        sol: Solution,
        ):
    assert sol.strstr("hello", "ll") == 2

def test_i_unicycle_returns_2(
        sol: Solution,
        ):
    assert sol.strstr("unicycle", "i") == 2

def test_sat_ersatz_returns_2(
        sol: Solution,
        ):
    assert sol.strstr("ersatz", "sat") == 2

def test_fig_ersatz_returns_neg1(
        sol: Solution,
        ):
    assert sol.strstr("ersatz", "fig") == -1

def test_fig_transfigure_returns_5(
        sol: Solution,
        ):
    assert sol.strstr("transfigure", "fig") == 5
