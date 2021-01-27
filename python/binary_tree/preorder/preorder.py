
# Given the root of a binary tree, return the preorder traversal 
# of its nodes' values.

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

from TreeNode import TreeNode

class Solution:

    def __init__(self):
        self.__visited = []

    def preorder_traversal(self, root: TreeNode) -> list:
        if root is None:
            return 
        self.__visited.append(root.val)
        self.preorder_traversal(root.left)
        self.preorder_traversal(root.right) 
        return self.__visited


if __name__ == "__main__":
    Solution()

