"""
author: buppter
datetime: 2019-08-12 20:02

题目描述：
输入一个链表，反转链表后，输出新链表的表头。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead: ListNode) -> ListNode:
        if not pHead:
            return pHead
        p = None
        while pHead:
            cur = pHead
            pHead = pHead.next
            cur.next = p
            p = cur
        return p
