
import unittest
from TreeNode import TreeNode
from postorder import Solution

class TestPostorder(unittest.TestCase):

    def test_1_null_2_returns_2_1(self):
        btree = [TreeNode(1), TreeNode(2)]
        btree[0].right = btree[1]
        self.assertEqual(Solution().postorder_traversal(btree[0]), [2, 1])

    def test_1_2_returns_2_1(self):
        btree = [TreeNode(1), TreeNode(2)]
        btree[0].left = btree[1]
        self.assertEqual(Solution().postorder_traversal(btree[0]), [2, 1])

    def test_1_returns_1(self):
        self.assertEqual(Solution().postorder_traversal(TreeNode(1)), [1])

    def test_1_null_2_3_returns_3_2_1(self):
        btree = list(TreeNode(i) for i in range(1, 4))
        btree[0].right = btree[1] 
        btree[1].left = btree[2]
        self.assertEqual(Solution().postorder_traversal(btree[0]), [3, 2, 1])

if __name__ == "__main__":
    unittest.main()
