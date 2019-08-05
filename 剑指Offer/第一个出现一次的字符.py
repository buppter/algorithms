"""
author: buppter
datetime: 2019-08-05 20:50

题目描述：
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置,
如果没有则返回 -1（需要区分大小写）.
"""


class Solution:
    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1
        for k, i in enumerate(s):
            if s.count(i) == 1:
                return k
