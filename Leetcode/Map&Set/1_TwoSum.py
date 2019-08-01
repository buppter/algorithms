"""
author: buppter
datetime: 2019-08-01 15:51

题目描述：
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

示例：
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

解题思路：
利用 Map
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for k, i in enumerate(nums):
            if target - i in d:
                return [d[target - i], k]
            else:
                d[i] = k
