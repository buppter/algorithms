"""
author: buppter
datetime: 2019/9/12 11:06
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.dfs(root, root)

    def dfs(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False

        return node1.val == node2.val and self.dfs(node1.left, node2.right) and self.dfs(node1.right, node2.left)
