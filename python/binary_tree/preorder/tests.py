
import unittest
from preorder import Solution
from TreeNode import TreeNode

class TestPreorder(unittest.TestCase):

    def test_1null23_returns_123(self):
        expected = [1, 2, 3,]
        nodes = list(map(lambda i: TreeNode(i), expected))
        nodes[0].right = nodes[1]
        nodes[1].left = nodes[-1]
        observed = Solution().preorder_traversal(nodes[0])
        self.assertEqual(observed, expected)

    def test_1_returns_1(self):
        observed = Solution().preorder_traversal(TreeNode(1))
        self.assertEqual(observed, [1,])

    def test_1_null_2_returns_1_2(self):
        a_root = TreeNode(1)
        a_root.right = TreeNode(2)
        observed = Solution().preorder_traversal(a_root)
        self.assertEqual(observed, [1, 2,])

    def test_1_2_returns_1_2(self):
        nodes = list(TreeNode(i) for i in range(1, 3))
        a_root = TreeNode(1)
        a_root.left = TreeNode(2) 
        observed = Solution().preorder_traversal(a_root)
        self.assertEqual(observed, [1, 2])

    def test_only_left_children_size_5_returns(self):
        expected = list(range(0, 26, 5))
        nodes = list(TreeNode(i) for i in expected)
        i = 0 
        while i < len(nodes) - 1:
            nodes[i].left = nodes[i + 1]
            i += 1
        observed = Solution().preorder_traversal(nodes[0])
        self.assertEqual(expected, observed)

    def test_3_1_2_returns_3_1_2(self):
        expected = [3, 1, 2,]
        a_root = TreeNode(3)
        a_root.left = TreeNode(1)
        a_root.right = TreeNode(2)
        observed = Solution().preorder_traversal(a_root)
        self.assertEqual(observed, expected)


if __name__ == "__main__":
    unittest.main()
