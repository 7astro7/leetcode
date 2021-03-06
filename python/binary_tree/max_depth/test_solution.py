
import pytest
from TreeNode import TreeNode
from max_depth_binary_tree import Solution

@pytest.fixture
def node9():
    return TreeNode(9)

@pytest.fixture
def node_none():
    return TreeNode(None)

@pytest.fixture
def root_of_2_node_tree():
    return TreeNode(val = -57, right = TreeNode(-83))

@pytest.fixture
def root_of_depth_5_tree():
    nodes = list(TreeNode(i) for i in (4, -100, -9, -52, -4,))
    nodes[0].right = nodes[1]
    nodes[1].left = nodes[2]
    nodes[2].right = nodes[3]
    nodes[3].left = nodes[4]
    for i in range(len(nodes) - 1):
        if not i % 2: 
            nodes[i].right = nodes[i + 1] 
        else:
            nodes[i].left = nodes[i + 1]
    return nodes[0]

def test_one_node_tree_returns_1(node9):
    assert Solution().max_depth(node9) == 1

def test_empty_tree_returns_0(node_none):
    assert Solution().max_depth(node_none) == 0

def test_root_of_2_node_tree_returns_2(root_of_2_node_tree):
    assert Solution().max_depth(root_of_2_node_tree) == 2

def test_max_depth_5_works(root_of_depth_5_tree):
    assert Solution().max_depth(root_of_depth_5_tree) == 5

