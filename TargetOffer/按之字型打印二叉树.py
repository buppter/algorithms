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

        flag = 1
        stack = [pRoot]
        res = []
        while stack:
            size = len(stack)
            cur_list = []
            for _ in range(size):
                node = stack.pop(0)
                cur_list.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            if flag == 1:
                res.append(cur_list)
            else:
                res.append(cur_list[::-1])
            flag *= -1
        return res
