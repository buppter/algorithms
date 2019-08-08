"""
author: buppter
datetime: 2019/8/8 15:29

题目描述：
判断一个数是否为2的n次幂
Given an integer, write a function to determine if it is a power of two.


示例：
Input: 1
Output: true
Explanation: 2^0 = 1

Input: 16
Output: true
Explanation: 2^4 = 16

Input: 218
Output: false


解题思路：
位运算
如果是2的N次方，那么二进制里有且只有一个1

"""


class Solution(object):

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and bin(n).count('1') == 1

    def isPowerOfTwo2(self, n):
        return n > 0 and n & (n - 1) == 0
