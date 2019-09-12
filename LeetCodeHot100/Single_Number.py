"""
author: buppter
datetime: 2019/9/12 11:44
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = {}

        for i in nums:
            if i in res:
                res.pop(i)
            else:
                res[i] = 1
        return res.popitem()[0]

    def singleNumber2(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res
