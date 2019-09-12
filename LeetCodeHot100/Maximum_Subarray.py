"""
author: buppter
datetime: 2019/9/12 10:11
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = [0 for _ in range(len(nums))]
        res[0] = nums[0]

        for i in range(1, len(nums)):
            res[i] = max(res[i - 1] + nums[i], nums[i])
        return max(res)
