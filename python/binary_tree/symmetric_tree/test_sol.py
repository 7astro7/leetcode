
import pytest
from symmetric_tree import (
        Solution, 
        TreeNode,
)

@pytest.fixture
def sol() -> Solution:
    return Solution()

@pytest.fixture
def island_root_returns_ok(
        sol: Solution,
        ) -> bool:
    return sol.is_symmetric(TreeNode(53))

def test_island_root(
        island_root_returns_ok: bool,
        ):
    assert island_root_returns_ok == True

@pytest.fixture
def one_child_asymmetric_returns_ok(
        sol: Solution,
        ) -> bool:
    a_root = TreeNode(53, left = TreeNode(57))
    if sol.is_symmetric(a_root):
        return False
    a_root = TreeNode(3, right = TreeNode(7))
    if sol.is_symmetric(a_root):
        return False
    return True

def test_one_child_asymmetric(
        one_child_asymmetric_returns_ok: bool,
        ):
    assert one_child_asymmetric_returns_ok == True

@pytest.fixture
def height1_symmetric_returns_ok(
        sol: Solution,
        ) -> bool:
    a_root = TreeNode(53, left = TreeNode(57))
    a_root.right = TreeNode(57)
    return sol.is_symmetric(a_root)

def test_height1_symmetric(
        height1_symmetric_returns_ok: bool,
        ):
    assert height1_symmetric_returns_ok == True

@pytest.fixture
def height2_asymmetric_returns_ok(
        sol: Solution,
        ) -> bool:
    a_root = TreeNode(53, left = TreeNode(57))
    a_root.right = TreeNode(57)
    a_root.right.right = TreeNode(13)
    return not sol.is_symmetric(a_root)

def test_height2_asymmetric(
        height2_asymmetric_returns_ok: bool,
        ):
    assert height2_asymmetric_returns_ok == True

@pytest.fixture
def symmetric_tree_sorted_from_1_returns_ok(
        sol: Solution,
        ) -> bool:
    nodes = tuple(TreeNode(i) for i in (1, 2, 2, 3, 4, 4, 3,))
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]
    nodes[2].left = nodes[-2]
    nodes[2].right = nodes[-1]
    return sol.is_symmetric(nodes[0])

def test_symmetric_tree_sorted_from_1(
        symmetric_tree_sorted_from_1_returns_ok: bool,
        ):
    assert symmetric_tree_sorted_from_1_returns_ok == True
    
@pytest.fixture
def asymmetric_tree_sorted_from_1_returns_ok(
        sol: Solution,
        ) -> bool:
    nodes = tuple(TreeNode(i) for i in (1, 2, 2, 3, 3,))
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].right = nodes[3]
    nodes[2].right = nodes[-1]
    return not sol.is_symmetric(nodes[0])

def test_asymmetric_tree_sorted_from_1(
        asymmetric_tree_sorted_from_1_returns_ok: bool,
        ):
    assert asymmetric_tree_sorted_from_1_returns_ok == True

@pytest.fixture
def maximally_imbalanced_tree_height_4_returns_ok(
        sol: Solution,
        ) -> bool:
    nodes = tuple(TreeNode(i) for i in (17, 19, 23, 29, 31,))
    for i in range(len(nodes) - 1):
        nodes[i].left = nodes[i + 1]
    return not sol.is_symmetric(nodes[0])

def test_maximally_imbalanced_tree_height_4(
        maximally_imbalanced_tree_height_4_returns_ok: bool,
        ):
    assert maximally_imbalanced_tree_height_4_returns_ok == True

@pytest.fixture
def symmetric_tree_height_4_returns_ok(
        sol: Solution,
        ) -> bool:
    nodes = tuple(TreeNode(i) for i in (17, 19, 19, 23, 23, 29, 29,))
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[2].right = nodes[4]
    nodes[3].right = nodes[5]
    nodes[4].left = nodes[6]
    return sol.is_symmetric(nodes[0])

def test_symmetric_tree_height_4(
        symmetric_tree_height_4_returns_ok: bool,
        ):
    assert symmetric_tree_height_4_returns_ok == True

@pytest.fixture
def asymmetric_at_level_3_tree_returns_ok(
        sol: Solution,
        ) -> bool:
    node_vals = (4,6,6,8,10,10,8,16,18,18,16,)
    nodes = tuple(TreeNode(i) for i in node_vals)
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]
    nodes[2].left = nodes[5]
    nodes[2].right = nodes[6]
    nodes[4].left = nodes[7]
    nodes[4].right = nodes[8]
    nodes[6].left = nodes[9]
    nodes[6].right = nodes[-1]
    return not sol.is_symmetric(nodes[0])


def test_asymmetric_at_level_3_tree(
        asymmetric_at_level_3_tree_returns_ok: bool,
        ):
    assert asymmetric_at_level_3_tree_returns_ok == True


