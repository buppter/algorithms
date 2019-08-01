"""
author: buppter
datetime: 2019/7/31 14:41

题目描述：
滑动窗口
Given an array nums, there is a sliding window of size k which is moving from the very
left of the array to the very right.
You can only see the k numbers in the window. Each time the sliding window moves
right by one position. Return the max sliding window.

示例：
Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        windows, res = [], []
        for i, x in enumerate(nums):
            if i >= k and windows[0] <= i - k:
                windows.pop(0)
            while windows and nums[windows[-1]] <= x:
                windows.pop()
            windows.append(i)
            if i >= k - 1:
                res.append(nums[windows[0]])
        return res
