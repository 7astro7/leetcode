"""
 Given the root of a binary tree, check whether it is a mirror of 
 itself (i.e., symmetric about its center)

 Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100
"""

from queue import SimpleQueue

# from leetcode
class TreeNode:

    def __init__(
            self,
            val = 0,
            left = None,
            right = None,
            ):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def _max_depth(
            self,
            a_root: TreeNode,
            ) -> int:
        if a_root is None or a_root.val is None:
            return 0
        if a_root.left is None and a_root.right is None:
            return 1
        depth_left = self._max_depth(a_root.left)
        depth_right = self._max_depth(a_root.right)
        return 1 + max(depth_left, depth_right)

    def is_symmetric(
            self, 
            root: TreeNode,
            ) -> bool:
        if root.left is None or root.right is None:
            if root.left != root.right:
                return False
            return True
        if root.left.val != root.right.val:
            return False
        if self._max_depth(root.left) != self._max_depth(root.right):
            return False
        # do BFS 
        Q, visited = SimpleQueue(), dict()
        Q.put((0, root,))
        exists = lambda vertex: vertex is not None
        is_unvisited = lambda vertex: not vertex in visited.keys()
        level_matrix = [[]]
        while not Q.empty():
            level, node = Q.get()
            if len(level_matrix) < level + 1:
                level_matrix.append([])
            visited[node] = level
            adj = tuple(filter(exists, (node.left, node.right,)))
            if not len(adj):
                node.val *= 3
            for v in tuple(filter(is_unvisited, adj)):
                if v is node.left: # denote that node is left child
                    v.val = -v.val
                Q.put((level + 1, v))
        for node, level in visited.items():
            level_matrix[level].append(node.val)
        for row in level_matrix[1:]:
            if sum(row):
                return False
        return True


