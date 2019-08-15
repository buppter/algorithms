"""
author: buppter
datetime: 2019/8/15 15:40


题目描述
输入一棵二叉树，判断该二叉树是否是平衡二叉树。


解决思路：
平衡二叉树特性：
它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def IsBalanced_Solution1(self, pRoot: TreeNode) -> bool:
        if not pRoot:
            return True
        if abs(self.depth(pRoot.left) - self.depth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution1(pRoot.left) and self.IsBalanced_Solution1(pRoot.right)

    def depth(self, pRoot):
        if not pRoot:
            return 0
        left = self.depth(pRoot.left)
        right = self.depth(pRoot.ritht)
        return max(left, right) + 1

    def IsBalanced_Solution2(self, pRoot: TreeNode) -> bool:
        if not pRoot:
            return True
        self.isbalanced = True
        self.getDepth(pRoot)
        return self.isbalanced

    def getDepth(self, pRoot):
        if not pRoot:
            return 0
        left = self.getDepth(pRoot.left)
        right = self.getDepth(pRoot.right)

        if abs(left - right) > 1:
            self.isbalanced = False
        return max(left, right) + 1
