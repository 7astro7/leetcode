
import unittest
from preorder import Solution
from TreeNode import TreeNode

class TestPreorder(unittest.TestCase):

    def test_1null23_returns_123(self):
        pre_nodes = [1, 2, 3,]
        btree = list(map(lambda i: TreeNode(i), pre_nodes))
        btree[0].right = btree[1]
        btree[1].left = btree[-1]
        btree_answer = Solution().preorder_traversal(btree[0])
        print(btree_answer)
        self.assertEqual(btree_answer, pre_nodes)

    def test_1_returns_1(self):
        self.assertEqual(Solution().preorder_traversal(TreeNode(1)), [1])

    def test_1_null_2_returns_1_2(self):
        btree = list(TreeNode(i) for i in range(1, 3))
        btree[0].right = btree[1] 
        self.assertEqual(Solution().preorder_traversal(btree[0]), [1, 2])

    def test_1_2_returns_1_2(self):
        btree = list(TreeNode(i) for i in range(1, 3))
        btree[0].left = btree[1] 
        self.assertEqual(Solution().preorder_traversal(btree[0]), [1, 2])

    def test_only_left_children_size_5_returns(self):
        btree = list(TreeNode(i) for i in range(0, 26, 5))
        i = 0 
        while i < len(btree) - 1:
            btree[i].left = btree[i + 1]
            i += 1
        self.assertEqual(Solution().preorder_traversal(btree[0]), [0, 5, 10, 15, 20, 25])

    def test_3_1_2_returns_3_1_2(self):
        btree = [TreeNode(i) for i in (3, 1, 2,)] 
        btree[0].left = btree[1]
        btree[0].right = btree[2] 
        self.assertEqual(Solution().preorder_traversal(btree[0]), [3, 1, 2,])


if __name__ == "__main__":
    unittest.main()
