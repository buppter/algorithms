"""
author: buppter
datetime: 2019-08-05 15:39

题目描述：
请实现一个函数按照之字形打印二叉树，
即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        queue = [pRoot]
        res = []
        flag = 1
        while queue:
            line = []
            size = len(queue)
            if size == 1:
                cur = queue[0]
                line.append(cur.val)
            else:
                if flag > 0:
                    for i in range(size):
                        line.append(queue[i].val)
                else:
                    for i in range(size, 0, -1):
                        line.append(queue[i-1].val)
            res.append(line)
            for i in range(size):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            flag = -flag
        return res

