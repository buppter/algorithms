"""
author: buppter
datetime: 2019/8/13 14:20

题目描述
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）


解决思路：
1. 遍历该链表,复制每一个节点,插入到当前节点的后面.形成如下链表.1->1'->2->2'....
2. 将每个拷贝节点的随机指针域,指向原节点(即拷贝节点的上一个节点)的随即指针域指向(注意随机指针域可能为空)的下一个节点.
即1的随机指针域指向3,则1'的随机指针域指向3的下一个指针3'.
3. 拆分链表,返回1'->2'->3'...
"""


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return None
        CloneNodes = self.CloneNodes(pHead)
        CloneRandom = self.CloneRandom(CloneNodes)
        CloneHead = self.ReconnectNodes(CloneRandom)
        return CloneHead

    # 复制节点，将复制的结点连接在原结点的后边
    def CloneNodes(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = RandomListNode(pNode.label)
            pCloned.next = pNode.next
            pNode.next = pCloned
            pNode = pCloned.next
            print(pCloned, pCloned.random, pCloned.label)

        return pHead

    # 将复制后的结点的随机指针指向原结点的随机指针的下一个结点
    def CloneRandom(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = pNode.next
            if pNode.random:
                pCloned.random = pNode.random.next
            pNode = pCloned.next
            print(pCloned, pCloned.random, pCloned.label)

        return pHead

    # 拆分链表
    def ReconnectNodes(self, pHead):
        pCloneHead = pCloneNode = pHead.next
        cur = pHead
        cur.next = pCloneNode.next
        cur = cur.next
        while cur:
            pCloneNode.next = cur.next
            pCloneNode = pCloneNode.next
            cur.next = pCloneNode.next
            cur = cur.next
        return pCloneHead

