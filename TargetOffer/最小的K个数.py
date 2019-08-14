"""
author: buppter
datetime: 2019/8/14 16:14


题目描述
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

解决思路：
1. 排序返回前4个数
2. 建立小顶堆
"""


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput or k > len(tinput):
            return []
        tinput.sort()
        return tinput[:k]
