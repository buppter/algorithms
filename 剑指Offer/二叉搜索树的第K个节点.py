"""
author: buppter
datetime: 2019-08-05 16:44

题目描述：
给定一棵二叉搜索树，请找出其中的第k小的结点。
例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。

解题思路：
二叉搜索树的中序遍历为递增的
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if not pRoot or not k:
            return None
        res = []
        self.inner(pRoot, res)
        if k <= len(res):
            return res[k - 1]
        return None

    def inner(self, pRoot, res):
        if not pRoot:
            return
        self.inner(pRoot.left, res)
        res.append(pRoot.val)
        self.inner(pRoot.right, res)
