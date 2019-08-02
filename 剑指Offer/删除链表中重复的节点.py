"""
author: buppter
datetime: 2019-08-02 22:40

题目描述：
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，
重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

结题思路：
三指针，既要记录头结点位置，也要记录当前节点的前一个节点位置
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead: ListNode) -> ListNode:
        if not pHead or not pHead.next:
            return pHead
        d = pre = ListNode(-1)
        d.next = pHead
        cur = pHead
        while cur:
            if cur.next and cur.val == cur.next.val:
                temp = cur.next
                while temp and temp.val == cur.val:
                    temp = temp.next
                cur = temp
                pre.next = temp
            else:
                pre = cur
                cur = cur.next
        return d.next


