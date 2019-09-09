"""
author: buppter
datetime: 2019/9/9 10:43
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []

        dic = {}
        for k, v in enumerate(nums):
            if (target - v) in dic:
                return [dic[target - v], k]
            else:
                dic[v] = k
