"""
author: buppter
datetime: 2019-08-02 21:59

题目描述：
从上往下打印出二叉树的每个节点，同层节点从左至右打印。

结题思路：
广度优先遍历(BFS)
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root: TreeNode) -> List[int]:
        # write code here
        if not root:
            return []
        queue = []
        res = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
