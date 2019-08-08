"""
author: buppter
datetime: 2019/8/8 11:11

题目描述：
树的最小深度
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.


示例：
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

解题思路：
BFS
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        count = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.pop(0)
                if not cur.right and not cur.left:
                    return count
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            count += 1
