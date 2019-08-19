"""
author: buppter
datetime: 2019/8/19 12:43

题目描述
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，
第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。

输出描述:
如果当前字符流没有存在出现一次的字符，返回#字符。
"""


class Solution:
    def __init__(self):
        self.dic = {}
        self.s = ''

    # 返回对应char
    def FirstAppearingOnce(self):
        for i in self.s:
            if self.dic[i] == 1:
                return i
        return "#"

    def Insert(self, char):
        self.s += char
        if char in self.dic:
            self.dic[char] += 1
        else:
            self.dic[char] = 1
