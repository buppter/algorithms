"""
author: buppter
datetime: 2019-08-12 19:42


题目描述：
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？


解决思路：
动态规划
当 n = 1: dp[1] = 1
n = 2: dp[2] = 2   横横或竖竖
n = 3: dp[3] = dp[1] + dp[2]
...
dp[n] = dp[n-1] + dp[n-2]

斐波那契数列问题
"""


class Solution:
    def rectCover(self, number: int) -> int:
        if number == 0:
            return 0
        a, b, c = 1, 0, 0
        while c < number:
            a, b = a + b, a
            c += 1
        return a
