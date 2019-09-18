"""
author: buppter
datetime: 2019/9/18 17:03
"""
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            if digits[i] == 10:
                carry = digits[i] // 10
                digits[i] %= 10
            else:
                return digits
        if carry:
            digits.insert(0, carry)
        return digits
