"""
author: buppter
datetime: 2019/8/12 15:25

题目描述：
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

解决思路：
1.利用二进制的运算 n & (n-1)
2. bin(n).count('1')

负数补码计算： n & 0xffffffff
"""


class Solution:
    def NumberOf1(self, n: int) -> int:
        if n < 0:
            n = n & 0xffffffff
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count

    def NumberOf12(self, n: int) -> int:
        if n < 0:
            return bin(n & 0xffffffff).count('1')
        return bin(n & 0xffffffff).count('1')
