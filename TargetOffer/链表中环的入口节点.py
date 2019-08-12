"""
author: buppter
datetime: 2019-08-02 22:17

题目描述：
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

结题思路：
遍历链表，若环存在，则遇到的第一个重复的即为入口节点
"""


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        if not pHead:
            return None
        res = []
        while True:
            res.append(pHead)
            pHead = pHead.next
            if not pHead:
                return None
            if pHead in res:
                return pHead
