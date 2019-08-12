"""
author: buppter
datetime: 2019-08-12 19:53

题目描述：
输入一个链表，输出该链表中倒数第k个结点。


解决思路：
双指针，一个指针从header先走k步，然后两个指针同时走，当先前的指针指向null时，后边的指针指向的即为倒数第k的节点
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        if k > self.length(head):
            return None
        fast, cur = head, head
        for _ in range(k):
            fast = fast.next
        while fast:
            cur = cur.next
            fast = fast.next
        return cur

    def length(self, head: ListNode) -> int:
        count = 0
        while head:
            head = head.next
            count += 1
        return count
