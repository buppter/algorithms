"""
author: buppter
datetime: 2019/8/15 15:26

题目描述
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def TreeDepth1(self, pRoot):
        if not pRoot:
            return 0
        left = self.TreeDepth1(pRoot.left)
        right = self.TreeDepth1(pRoot.right)

        return max(left, right) + 1

    def TreeDepth2(self, pRoot):
        if not pRoot:
            return 0
        queue = [pRoot]
        deep = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            deep += 1
        return deep
