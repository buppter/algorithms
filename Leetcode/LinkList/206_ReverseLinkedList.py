"""
author: buppter
datetime: 2019/7/30 11:14

题目描述：
单链表反转

示例：
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

解题思路：
双指针法
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head: ListNode) -> ListNode:
        perv = None
        while head:
            cur = head
            head = cur.next
            cur.next = perv
            perv = cur
        return perv
