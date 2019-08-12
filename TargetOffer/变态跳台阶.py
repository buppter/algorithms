"""
author: buppter
datetime: 2019/8/12 15:48


题目描述：
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。


解决思路：
动态规划问题

dp[n] = dp[n-1] + dp[n-2] + dp[n-3] + ... + dp[n-(n-1)] + dp[n-n] = dp[0] + dp[1] + dp[2] + ... + dp[n-2] + dp[n-1]
dp[n-1] = dp[0] + dp[1] + dp[2] + ... + dp[n - 2]

====>
dp[n] = 2 * dp[n-1]
"""


class Solution:
    def jumpFloorII(self, number: int) -> int:
        if number == 1 or not number or number == 2:
            return number
        return 2 * self.jumpFloorII(number - 1)