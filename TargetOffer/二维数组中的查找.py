"""
author: buppter
datetime: 2019/8/21 12:58


题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""


class Solution:
    # array 二维列表
    def Find(self, target, array):
        if not target or not array:
            return False
        rows_len = len(array)
        rows = 0
        cols = len(array[0]) - 1
        while rows < rows_len and cols >= 0:
            if array[rows][cols] == target:
                return True
            elif array[rows][cols] < target:
                rows += 1
            else:
                cols -= 1
        return False

