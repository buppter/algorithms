"""
author: buppter
datetime: 2019/8/8 15:44

题目描述：
比特位计数
Given a non negative integer number num. For every numbers i in the
range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.


示例：
Input: 2
Output: [0,1,1]

Input: 5
Output: [0,1,1,2,1,2]


解题思路：
遍历 0-n，统计bin(n).count('1')
"""


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        for i in range(num + 1):
            res.append(bin(i).count('1'))
        return res


