"""
author: buppter
datetime: 2019/8/13 13:35

题目描述：
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

解决思路：
对于一个二叉树的后序遍历序列来说，最后一个数一定是根节点，然后前面的数中，
从最开始到第一个大于根节点的数都是左子树中的数，而后面到倒数第二个数应该都是大于根节点的，是右子树，
如果后面的数中有小于根节点的，那么说明这个序列不是二叉搜索树的后序遍历序列
"""


class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        root = sequence[-1]

        # 左子树
        i = 0
        while i < (len(sequence) - 1):
            if sequence[i] > root:
                break
            i += 1

        # 右子树
        j = i
        while j < (len(sequence) - 1):
            if sequence[j] < root:
                return False
            j += 1

        # 判断左子树
        left = True
        if i > 0:  # 表示左子树为空
            left = self.VerifySquenceOfBST(sequence[:i])
        right = True
        if i < (len(sequence) - 1):
            right = self.VerifySquenceOfBST(sequence[i: len(sequence) - 1])
        return left and right
