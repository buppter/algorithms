"""
author: buppter
datetime: 2019/8/15 15:05

题目描述
统计一个数字在排序数组中出现的次数。
"""


class Solution:
    def GetNumberOfK1(self, data, k):
        # write code here
        if not data or not k:
            return 0
        return data.count(k)

    def GetNumberOfK2(self, data, k):
        if not data or not k:
            return 0
        count = 0
        for i in data:
            if i == k:
                count += 1
        return count

    def GetNumberOfK3(self, data, k):
        if not data or not k:
            return 0
        if k not in data:
            return 0
        l = 0
        r = len(data) - 1

        while data[l] != k and l < r:
            l += 1
        while data[r] != k and l < r:
            r -= 1
        return r - l + 1
