"""
author: buppter
datetime: 2019/8/14 16:01

题目描述
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。


解决思路：
排序，找到中位数，判断中位数的次数是否超过数组长度的一半
"""


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers:
            return 0
        size = len(numbers)
        numbers.sort()
        res = numbers[size // 2]

        count = numbers.count(res)
        if count > size // 2:
            return res
        return 0
