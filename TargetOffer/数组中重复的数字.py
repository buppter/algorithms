"""
author: buppter
datetime: 2019-08-03 11:04

题目描述：
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

结题思路：
1. 借助Map
2. 先排序，然后遍历比较
"""
from typing import List


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers: List[int], duplication: List[int]) -> bool:
        if not numbers:
            return False
        res = []
        for i in numbers:
            if i not in res:
                res.append(i)
            else:
                duplication[0] = i
                return True
        return False

    def _duplicate(self, numbers: List[int], duplication: List[int]) -> bool:
        if not numbers:
            return False
        numbers.sort()
        for i in range(1, len(numbers)):
            if numbers[i] == numbers[i - 1]:
                duplication[0] = numbers[i]
                return True
        return False


