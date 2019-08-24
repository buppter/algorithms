"""
author: buppter
datetime: 2019-08-05 15:25

题目描述：
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if not pRoot:
            return []
        res = []

        stack = [pRoot]
        while stack:
            size = len(stack)
            cur_res = []

            for _ in range(size):
                node = stack.pop(0)

                cur_res.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res.append(cur_res)
        return res
