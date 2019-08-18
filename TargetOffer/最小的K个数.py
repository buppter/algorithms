"""
author: buppter
datetime: 2019/8/14 16:14


题目描述
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

解决思路：
1. 排序返回前4个数
2. 建立小顶堆
3. 快排思想
"""


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput or k > len(tinput):
            return []
        tinput.sort()
        return tinput[:k]

    def GetLeastNumbers_Solution1(self, tinput, k):
        if not tinput or k > len(tinput) or not k:
            return []
        start = 0
        end = len(tinput) - 1
        s = self.quick_sort(tinput, start, end)
        while s + 1 != k:
            if s + 1 > k:
                end = s - 1
            if s + 1 < k:
                start = s + 1
            s = self.quick_sort(tinput, start, end)

        return tinput[:k]

    def quick_sort(self, alist, start, end):
        if start > end:
            return
        low = start
        high = end
        mid = alist[start]

        while low < high:
            while alist[high] >= mid and low < high:
                high -= 1
            alist[low] = alist[high]
            while alist[low] < mid and low < high:
                low += 1
            alist[high] = alist[low]
        alist[low] = mid
        return low
