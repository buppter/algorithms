"""
author: buppter
datetime: 2019/8/8 14:36

题目描述：
二进制数中1的个数
Write a function that takes an unsigned integer and return the number of '1' bits it has
(also known as the Hamming weight).


示例：
Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.


解题思路：
做位运算
"""


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 0:
            count += 1
            n = n & (n - 1)
        return count
