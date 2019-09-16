"""
author: buppter
datetime: 2019/9/16 10:56
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or not n:
            return head
        len = self.get_length(head)

        if len == n:
            return head.next
        pre = cur = head
        for _ in range(n):
            cur = cur.next
        while cur.next:
            cur = cur.next
            pre = pre.next

        pre.next = pre.next.next

        return head

    def get_length(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count
