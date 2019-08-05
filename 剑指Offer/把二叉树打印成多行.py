"""
author: buppter
datetime: 2019-08-05 15:25

题目描述：
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if not pRoot:
            return []
        queue = [pRoot]
        res = []

        while queue:
            line = []
            size = len(queue)
            for i in queue:
                line.append(i.val)
            res.append(line)

            for i in range(size):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return res
