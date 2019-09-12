"""
author: buppter
datetime: 2019/9/12 10:22
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            root = l1
            root.next = self.mergeTwoLists(l1.next, l2)
        else:
            root = l2
            root.next = self.mergeTwoLists(l1, l2.next)
        return root
