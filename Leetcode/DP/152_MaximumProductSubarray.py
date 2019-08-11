"""
author: buppter
datetime: 2019/8/11 15:17

题目描述：
乘积最大子序列
Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.


示例：
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


解题思路：

"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [[0 for _ in range(2)] for _ in range(2)]
        dp[0][1], dp[0][0], res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            x, y = i % 2, (i - 1) % 2
            dp[x][0] = max(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            dp[x][1] = min(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            res = max(res, dp[x][0])
        return res
