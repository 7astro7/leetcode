
import unittest
from TreeNode import TreeNode
from levelorder import Solution

class testLevelOrder(unittest.TestCase):

    def test_3_9_20_15_7_returns_3_then_9_and_20_then_15_and7(self):
        expected = [[3,], [9, 20,], [15, 7,],]
        nodes = [TreeNode(i) for i in (3, 9, 20, 15, 7,)]
        nodes[0].left = nodes[1]
        nodes[0].right = nodes[2]
        nodes[2].left = nodes[-2]
        nodes[2].right = nodes[-1]
        self.assertEqual(Solution().level_order(nodes[0]), expected)

    def test_1_node_returns_1_node_1_level(self):
        a_node = TreeNode(93)
        expected = [[93,],]
        self.assertEqual(Solution().level_order(a_node), expected)

    def test_imbalanced_left_returns_5_levels(self):
        nodes = [[TreeNode(i),] for i in range(47, 52)]
        for j in range(len(nodes) - 1):
            nodes[j][0].left = nodes[j + 1][0]
        expected = [[level[0].val,] for level in nodes]
        observed = Solution().level_order(nodes[0][0])
        self.assertEqual(observed, expected)

    def test_imbalanced_right_returns_5_levels(self):
        nodes = [[TreeNode(i),] for i in range(47, 52)]
        for j in range(len(nodes) - 1):
            nodes[j][0].right = nodes[j + 1][0]
        expected = [[level[0].val,] for level in nodes]
        observed = Solution().level_order(nodes[0][0])
        self.assertEqual(observed, expected)

    def test_left_nodes_visited_first(self):
        expected = [[71,], [81, 4,], [44,-5,]]
        a_root = TreeNode(71)
        a_root.left = TreeNode(81)
        a_root.right = TreeNode(4)
        a_root.right.left = TreeNode(44)
        a_root.right.right = TreeNode(-5)
        self.assertEqual(Solution().level_order(a_root), expected)

    def test_nullroot_returns_empty_list(self):
        self.assertEqual(Solution().level_order(None), [])



if __name__ == "__main__":
    unittest.main()

