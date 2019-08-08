"""
author: buppter
datetime: 2019/8/8 11:09

题目描述：
求树的最大深度
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.


示例：
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.


解题思路：
BFS
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        res = []
        count = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.pop(0)
                if not cur.left and not cur.right:
                    res.append(count)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            count += 1
        return max(res)

