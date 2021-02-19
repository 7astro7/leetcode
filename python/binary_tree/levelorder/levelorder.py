
# Given a binary tree, return the level order traversal of its 
# nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree: [3,9,20,null,null,15,7],

#    3
#   / \
#  9  20
#    /  \
#   15   7

# return its level order traversal as:

#[
#  [3],
#  [9,20],
#  [15,7]
#]

from TreeNode import TreeNode
from queue import SimpleQueue

class Solution:

    def __init__(self):
        self.__visited = dict()
        self.__Q = SimpleQueue()

    def level_order(self, root: TreeNode) -> list:  # BFS
        if root is None:
            return []
        self.__Q.put((0, root))
        exists = lambda node: node is not None
        not_visited = lambda node: node not in self.__visited.keys()
        while not self.__Q.empty():
            level, node = self.__Q.get()
            self.__visited[node] = level
            adjacent = tuple(filter(exists, (node.left, node.right)))
            adjacent = tuple(filter(not_visited, adjacent))
            for adj_node in adjacent:
                self.__Q.put((level + 1, adj_node,))
        level_vector = list([] for v in set(self.__visited.values()))
        for vertex, level in self.__visited.items():
            level_vector[level].append(vertex.val)
        return level_vector


if __name__ == "__main__":
    Solution()
