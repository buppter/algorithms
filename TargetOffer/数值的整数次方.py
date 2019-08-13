"""
author: buppter
datetime: 2019/8/13 12:48

题目描述：
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。


解决思路：
1. 边界条件
2. 对于exponent 为偶数情况，即为 base^(exponent//2) * base^(exponent//2)
3. 对于exponent为奇数情况，即为 base^(exponent//2) * base^(exponent//2) * base
4. 使用 exponent >> 1 代替 exponent // 2
5. 使用 exponent & 1 代替 exponent % 2
"""


class Solution:
    def Power(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        if exponent == -1:
            return 1 / base

        result = self.Power(base, exponent >> 1)
        result *= result

        if (exponent % 2) == 1:
            result *= base
        return result
