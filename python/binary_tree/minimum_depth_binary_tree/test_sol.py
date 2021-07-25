
import pytest
from minimum_depth_binary_tree import TreeNode, Solution

@pytest.fixture
def sol() -> Solution:
    return Solution()

def test_1node_returns_1(sol: Solution):
    assert sol.min_depth(TreeNode(9)) == 1

def test_0node_returns_0(sol: Solution):
    assert sol.min_depth(None) == 0

def test_2_returns_2(sol: Solution):
    root = TreeNode(3, left = TreeNode(32)) 
    assert sol.min_depth(root) == 2

def test_tree1_returns_2(sol: Solution):
    root = TreeNode(3, left = TreeNode(9), right = TreeNode(20)) 
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert sol.min_depth(root) == 2

def test_tree2_returns_3(sol: Solution):
    root = TreeNode(3, left = TreeNode(9), right = TreeNode(20)) 
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    root.left.left = TreeNode(11)
    assert sol.min_depth(root) == 3

def test_tree3_returns_3(sol: Solution):
    root = TreeNode(3, left = TreeNode(9), right = TreeNode(20)) 
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    root.left.left = TreeNode(11)
    root.right.left.left = TreeNode(52)
    root.right.right.right = TreeNode(2)
    assert sol.min_depth(root) == 3

def test_tree4_returns_5(sol: Solution):
    root = TreeNode(2, right = TreeNode(3))
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(5)
    root.right.right.right.right = TreeNode(6)
    assert sol.min_depth(root) == 5





