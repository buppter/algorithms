"""
author: buppter
datetime: 2019/9/16 10:18
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, head1, head2):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not head1 or not head2:
            return None
        len1 = self.get_length(head1)
        len2 = self.get_length(head2)

        step = abs(len1 - len2)
        if len1 > len2:
            fast = head1
            for _ in range(step):
                fast = fast.next
            slow = head2

        else:
            fast = head2
            for _ in range(step):
                fast = fast.next
            slow = head1

        while fast or slow:
            if fast is slow:
                return fast
            else:
                fast = fast.next
                slow = slow.next
        return None

    def get_length(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count
