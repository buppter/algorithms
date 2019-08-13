"""
author: buppter
datetime: 2019/8/13 15:57

题目描述：
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        res = []
        self.inner(res, pRootOfTree)

        for i in range(len(res) - 1):
            res[i].right = res[i + 1]
            res[i + 1].left = res[i]
        return res[0]

    def inner(self, res, root):
        if not root:
            return
        self.inner(res, root.left)
        res.append(root)
        self.inner(res, root.right)
