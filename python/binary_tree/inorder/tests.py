
import unittest 
from TreeNode import TreeNode
from inorder import Solution 

class TestInorder(unittest.TestCase):

    def test_1_2_returns_2_1(self):
        btree = [TreeNode(i) for i in range(1, 3)] 
        btree[0].left = btree[1] 
        self.assertEqual(Solution().inorder_traversal(btree[0]), [2, 1])

    def test_1_returns_1(self):
        self.assertEqual(Solution().inorder_traversal(TreeNode(1)), [1])

    def test_1_null_2_3_returns_1_3_2(self):
        btree = list(TreeNode(i) for i in [1, 2, 3]) 
        btree[0].right = btree[1]
        btree[1].left = btree[-1]
        self.assertEqual(Solution().inorder_traversal(btree[0]), [1, 3, 2])

    def test_1_null_2_returns_1_2(self):
        btree = [TreeNode(1), TreeNode(2)]
        btree[0].right = btree[1]
        self.assertEqual(Solution().inorder_traversal(btree[0]), [1, 2])


if __name__ == "__main__":
    unittest.main()
