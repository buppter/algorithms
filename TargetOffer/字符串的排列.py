"""
author: buppter
datetime: 2019/8/14 14:54

题目描述：
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。


输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。


解决思路：
全排列
问题转换为先固定第一个字符，求剩余字符的排列；求剩余字符排列时跟原问题一样。
(1) 遍历出所有可能出现在第一个位置的字符（即：依次将第一个字符同后面所有字符交换）；
(2) 固定第一个字符，求后面字符的排列（即：在第1步的遍历过程中，插入递归进行实现）。
"""


class Solution:
    def Permutation(self, ss):
        if not ss:
            return []
        if len(ss) == 1:
            return [ss]

        pStr = []
        charlist = list(ss)
        charlist.sort()

        for i in range(len(charlist)):
            if i > 0 and charlist[i] == charlist[i - 1]:
                continue
            temp = self.Permutation(''.join(charlist[:i]) + ''.join(charlist[i + 1:]))
            for j in temp:
                pStr.append(charlist[i] + j)
        return pStr

