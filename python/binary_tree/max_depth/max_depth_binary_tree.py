
# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the 
# longest path from the root node down to the farthest leaf node.

# Example 1
#   Input: root = [3,9,20,null,null,15,7]
#   Output: 3

# Example 2:
#   Input: root = [1,null,2]
#   Output: 2

# Example 3:
#   Input: root = []
#   Output: 0

# Example 4:
#   Input: root = [0]
#   Output: 1

# Constraints:

#    The number of nodes in the tree is in the range [0, 10**4].
#    -100 <= Node.val <= 100

from TreeNode import TreeNode

class Solution: 

    def max_depth(self, root: TreeNode) -> int:
        if (root is None or root.val is None):
            return 0
        if root.left is None and root.right is None:
            return 1
        depth_left = self.max_depth(root.left)
        depth_right = self.max_depth(root.right)
        return 1 + max(depth_left, depth_right)
        

if __name__ == "__main__":
    Solution()