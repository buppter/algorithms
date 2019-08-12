"""
author: buppter
datetime: 2019/8/12 15:43


题目描述：
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。


解决思路：
动态规划思想
青蛙跳到最后一级可以是两级跳过来，也可以是一级跳过来，所以dp[n] = dp[n-1] + dp[n-2]
就变成了 斐波那切数列问题
"""


class Solution:
    def jumpFloor(self, n: int) -> int:
        a, b, c = 1, 0, 0
        while c < n:
            a, b = a + b, a
            c += 1
        return a
