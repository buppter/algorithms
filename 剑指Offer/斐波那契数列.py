"""
author: buppter
datetime: 2019-08-02 23:04

题目描述：
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39

结题思路：
1. 递归，但要记录已经产生的数值（也是动态规划问题）!!!但这种做法会超时
2. 公式
"""


class Solution:
    def Fibonacci(self, n: int) -> int:
        res = {0: 0, 1: 1, 2: 1}
        if n == 0 or n == 1 or n == 2:
            return res[n]
        elif res.get(n):
            return res[n]
        else:
            res[n] = self.Fibonacci(n - 1) + self.Fibonacci(n - 2)
            return res[n]

    def _Fibonacci(self, n: int) -> int:
        if n == 0:
            return 0
        else:
            a, b, c = 1, 0, 1
            while c < n:
                a, b = a + b, a
                c += 1
            return a
