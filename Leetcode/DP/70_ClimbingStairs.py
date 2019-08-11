"""
author: buppter
datetime: 2019/8/11 14:29

题目描述：
爬楼梯
Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


示例：
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


解题思路：
动态规划
f(n) = f(n-1） + f(n-2)
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0 or n == 1:
            return 1
        a, b, c = 1, 0, 0
        while c < n:
            a, b = a + b, a
            c += 1
        return a