"""
author: buppter
datetime: 2019/8/13 13:14

题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""


class Solution:
    def reOrderArray(self, array):
        res1 = []
        res2 = []

        for i in array:
            if i % 2 == 0:
                res1.append(i)
            else:
                res2.append(i)
        return res2 + res1
