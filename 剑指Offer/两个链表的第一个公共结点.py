"""
author: buppter
datetime: 2019/8/7 12:45

题目描述：
输入两个链表，找出它们的第一个公共结点。

解题思路：
1. 借助set，遍历保存链表1， 然后遍历链表2， 如果结点已经在Map中，则直接返回
2. 先判断两个链表的长度，然后长的减去短的，假设值为x，长的先走x步，然后两个指针同时走，直至相遇
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 方法1
    def FindFirstCommonNode(self, pHead1, pHead2):
        res = set()
        while pHead1:
            res.add(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            if pHead2 in res:
                return pHead2
            pHead2 = pHead2.next
        return None

    # 方法2
    def FindFirstCommonNode2(self, pHead1, pHead2):
        len1 = self.length(pHead1)
        len2 = self.length(pHead2)
        p1 = pHead1
        p2 = pHead2
        if len1 > len2:
            for i in range(len1 - len2):
                p1 = p1.next
        else:
            for i in range(len2 - len1):
                p2 = p2.next
        while p1 and p2:
            if p1 is p2:
                return p1
            p1 = p1.next
            p2 = p2.next
        return None

    def length(self, pHead):
        count = 0
        while pHead:
            pHead = pHead.next
            count += 1
        return count

