
import pytest
from search_in_a_bst import Solution, TreeNode

@pytest.fixture
def sol() -> Solution:
    return Solution()

@pytest.fixture
def root1() -> TreeNode:
    root = TreeNode(4, left = TreeNode(2), right = TreeNode(7))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    return root

def test_root1_val2(sol: Solution, root1: TreeNode):
    observed = sol.search_bst(root1, 2)
    assert observed.val == 2
    assert observed.left.val == 1
    assert observed.right.val == 3


def test_root1_val5(sol: Solution, root1: TreeNode):
    assert sol.search_bst(root1, 5) is None

@pytest.fixture
def root2() -> TreeNode:
    root = TreeNode(9, left = TreeNode(5), right = TreeNode(11))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    return root

def test_root2_val5(sol: Solution, root2: TreeNode):
    observed = sol.search_bst(root2, 5)
    assert observed.val == 5
    assert observed.left.val == 1
    assert observed.right.val == 6

