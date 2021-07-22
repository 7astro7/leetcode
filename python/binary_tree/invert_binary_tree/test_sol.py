
import pytest
from invert_binary_tree import Solution, TreeNode

@pytest.fixture
def sol() -> Solution:
    return Solution()

def test_null_root_returns_null(sol: Solution):
    assert sol.invert_tree(None) == None

@pytest.fixture
def tree1_returned_ok(sol: Solution):
    tree1 = tuple(TreeNode(i) for i in range(1, 4))
    tree1[0].left = tree1[2]
    tree1[0].right = tree1[1]
    returned = sol.invert_tree(tree1[0])
    if returned.left != tree1[1] or returned.right != tree1[2]:
        return False
    return True

def test_tree1(tree1_returned_ok: bool):
    assert tree1_returned_ok 

@pytest.fixture
def tree2_returned_ok(sol: Solution):
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    returned = sol.invert_tree(root)
    if returned.left.val != 7:
        return False
    if returned.right.val != 2:
        return False
    if returned.left.left.val != 9:
        return False
    if returned.left.right.val != 6:
        return False
    if returned.right.left.val != 3:
        return False
    if returned.right.right.val != 1:
        return False
    return True

def test_tree2(tree2_returned_ok: bool):
    assert tree2_returned_ok 

@pytest.fixture
def tree3_returned_ok(sol: Solution):
    root = TreeNode(5)
    root.left = TreeNode(10)
    root.right = TreeNode(4)
    root.left.left = TreeNode(15)
    root.right.right = TreeNode(3)
    returned = sol.invert_tree(root)
    if root.left.val != 4:
        return False
    if root.right.val != 10:
        return False
    if root.left.left.val != 3:
        return False
    if root.right.right.val != 15:
        return False
    return True

def test_tree3(tree3_returned_ok: bool):
    assert tree3_returned_ok 



