
# submission accepted on 2021-January-22 23:28 Pacific Time

# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Example 1:
#   Input: root = [1,null,2,3]
#   Output: [3,2,1]

# Example 2:
#   Input: root = []
#   Output: []

# Example 3:

#   Input: root = [1]
#   Output: [1]

# Example 4:
#   Input: root = [1,2]
#   Output: [2,1]

# Example 5:
#   Input: root = [1,null,2]
#   Output: [2,1]

# Constraints:
#    The number of the nodes in the tree is in the range [0, 100].
#    -100 <= Node.val <= 100

from TreeNode import TreeNode

class Solution:

    def __init__(self):
        self.__visited = [] 

    def postorder_traversal(self, root: TreeNode) -> list:
        if root is None:
            return 
        self.postorder_traversal(root.left)
        self.postorder_traversal(root.right)
        self.__visited.append(root.val)
        return self.__visited


if __name__ == "__main__":
    Solution()
