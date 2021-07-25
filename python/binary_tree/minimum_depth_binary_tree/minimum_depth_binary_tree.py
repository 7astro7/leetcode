
"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from
the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Constraints:
    The number of nodes in the tree is in the range [0, 1e5].
    -1000 <= Node.val <= 1000
"""

from queue import SimpleQueue

class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def min_depth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        q = SimpleQueue()
        visited, leaves = dict(), dict()
        q.put((1, root))
        while not q.empty():
            depth, node = q.get()
            visited[node] = depth
            if node.left is None and node.right is None:
                leaves[node] = depth
            else:
                for vertex in (node.left, node.right,):
                    if vertex and not vertex in visited.keys():
                        q.put((depth + 1, vertex,))
        return min(leaves.values())


