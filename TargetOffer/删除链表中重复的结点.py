"""
author: buppter
datetime: 2019/8/16 13:06

题目描述
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead: ListNode) -> ListNode:
        if not pHead or not pHead.next:
            return pHead
        p = pre = ListNode(-1)
        p.next = pHead

        cur = pHead

        while cur:
            if cur.next and cur.val == cur.next.val:
                tmp = cur.next
                while tmp.next and tmp.next.val == cur.val:
                    tmp = tmp.next
                cur = tmp.next
                pre.next = cur
            else:
                pre = cur
                cur = cur.next
        return p.next
