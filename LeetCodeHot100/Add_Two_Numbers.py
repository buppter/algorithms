"""
author: buppter
datetime: 2019/9/9 10:44
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = cur = ListNode(-1)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry if carry < 10 else carry - 10)
            carry = 0 if carry < 10 else 1
            cur = cur.next
        return l3.next
