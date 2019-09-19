"""
author: buppter
datetime: 2019/9/19 13:27


题目描述：
给定一个无序数组，包含正数、负数和0，要求从中找出3个数的乘积，使得乘积最大


解决思路：
定义五个数:一个最大,一个次大,一个第三大,一个最小,一个次小
然后求解即可
"""


class Solution:
    def find_max(self, alist):
        if not alist:
            return
        max1, max2, max3 = float("-inf"), float("-inf"), float("-inf")
        min1, min2 = float("inf"), format("inf")

        for i in alist:
            if i > max1:
                max1, max2, max3 = i, max1, max2
            elif i > max2:
                max2, max3 = i, max2
            elif i > max3:
                max3 = i

            if i < min1:
                min1, min2 = i, min1
            elif i < min2:
                min2 = i
        return max(max1 * max2 * max3, min1 * min2 * max1)
