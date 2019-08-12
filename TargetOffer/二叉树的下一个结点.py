"""
author: buppter
datetime: 2019-08-05 14:43

题目描述：
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

结题思路：
1. 如果当前结点右子树不空，那么中序下一个节点就是右子树的最左节点；如果右子树没有左子树就直接返回右子树根节点
2. 如果这个结点没有右子树，而该结点是其父结点的左结点，则该结点的下一个结点就是其父结点。
3. 若该节点也不是其父结点的左结点，则继续向上遍历其父节点的父节点，重复之前的判断，返回结果。


"""


# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return None
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        else:
            while pNode.next:
                if pNode.next.left == pNode:
                    return pNode.next
                pNode = pNode.next
            return None


