"""
author: buppter
datetime: 2019/8/2 16:34

题目描述：
求众数
Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears
more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

示例：
Input: [3,2,3]
Output: 3

Input: [2,2,1,1,1,2,2]
Output: 2

解题思路：
1. 利用字典统计次数
2. 排序，然后返回中间的值
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = {}
        for i in nums:
            if i not in res:
                res[i] = 1
            if res[i] > len(nums) // 2:
                return i
            else:
                res[i] += 1

    def _majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
