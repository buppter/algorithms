"""
author: buppter
datetime: 2019/9/18 15:28
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        i = head
        j = head.next
        even = head.next
        while i.next and j.next:
            i.next = j.next
            i = i.next
            j.next = i.next
            j = j.next
        i.next = even
        return head
