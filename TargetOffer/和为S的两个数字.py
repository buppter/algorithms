"""
author: buppter
datetime: 2019/8/15 16:34

题目描述
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。


解决思路：
1. 已经排序，所以可以使用双指针
2. 对于未排序的，可以使用 y = s - x，借助Map， LeetCode 第一题。但要判断最小乘积，略显的复杂
"""


class Solution:
    def FindNumbersWithSum1(self, array: list, tsum: int) -> list:
        if not array:
            return []
        l, r = 0, len(array) - 1

        while l < r:
            if array[l] + array[r] < tsum:
                l += 1
            elif array[l] + array[r] > tsum:
                r -= 1
            else:
                return [array[l], array[r]]
        return []

    def FindNumbersWithSum2(self, array: list, tsum: int) -> list:
        if not array:
            return []

        dic = {}
        res = []
        for i, v in enumerate(array):
            if tsum - v not in dic:
                dic[v] = i
            else:
                res.append([tsum - v, v])
        if len(res) == 1:
            return res[0]
        if not res:
            return []
        return self.getMin(res)

    def getMin(self, array):
        res = []
        for i in array:
            s = 1
            for l in i:
                s *= l
            res.append(s)
        return array[res.index(min(res))]

