"""
author: buppter
datetime: 2019-08-05 15:17

题目描述：
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetrical(self, pRoot):
        return self.isSymmetrical(pRoot, pRoot)

    def isSame(self, p1, p2):
        if p1 is None and p2 is None:
            return True
        if p1 is None or p2 is None:
            return False
        if p1.val != p2.val:
            return False
        return self.isSame(p1.left, p2.right) and self.isSame(p1.right, p2.left)
