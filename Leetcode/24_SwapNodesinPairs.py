"""
author: buppter
datetime: 2019/7/30 11:29

题目描述：
链表中的节点，两两反转
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.

示例：
Given 1->2->3->4, you should return the list as 2->1->4->3.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = prev = ListNode(0)
        dummy.next = head

        while head and head.next:
            tmp = head.next
            head.next = tmp.next
            tmp.next = head
            prev.next = tmp
            head = head.next
            prev = tmp.next
        return dummy.next
