"""
author: buppter
datetime: 2019/8/2 15:57

题目描述：
计算 x 的 n 次方
Implement pow(x, n), which calculates x raised to the power n (xn).

示例：
Input: 2.00000, 10
Output: 1024.00000

Input: 2.10000, 3
Output: 9.26100

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


解题思路：
分治，进行拆分
"""


class Solution:
    # 递归
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)

    # 非递归
    def _myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n % 2:
                pow *= x
            x *= x
            n //= 2
        return pow
