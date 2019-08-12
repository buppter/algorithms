"""
author: buppter
datetime: 2019-08-12 20:12

题目描述：
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1: ListNode, pHead2: ListNode) -> ListNode:
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        pHeadMerge = None
        if pHead1.val < pHead2.val:
            pHeadMerge = pHead1
            pHeadMerge.next = self.Merge(pHead1.next, pHead2)
        else:
            pHeadMerge = pHead2
            pHeadMerge.next = self.Merge(pHead1, pHead2.next)
        return pHeadMerge
