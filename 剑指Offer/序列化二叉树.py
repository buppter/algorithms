"""
author: buppter
datetime: 2019-08-05 20:02

题目描述：
请实现两个函数，分别用来序列化和反序列化二叉树
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Serialize(self, root):
        res = []
        self.pre(root, res)
        s = ",".join(res)
        return s

    def pre(self, root, res):
        if not root:
            res.append("null")
            return res
        res.append(root.val)
        self.pre(root.left, res)
        self.pre(root.right, res)

    def Deserialize(self, s):
        val = s.split(",")
        root, _ = self.deserialize(val, 0)
        return root

    def deserialize(self, s, index):
        if s[index] == "null":
            return None, index + 1
        root = TreeNode(int(s[index]))
        index += 1
        root.left, index = self.deserialize(s, index)
        root.right, index = self.deserialize(s, index)
        return root, index

if __name__ == "__main__":
    s = "1,2,4,5,3,6,null"
    sl = Solution()
    root = sl.Deserialize(s)
    print(root)
