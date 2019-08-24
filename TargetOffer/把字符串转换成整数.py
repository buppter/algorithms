"""
author: buppter
datetime: 2019/8/16 12:48


题目描述
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
"""


class Solution:
    def StrToInt(self, s: str) -> int:
        if not s:
            return 0
        flag = 1

        dic = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        if s[0] == "-":
            flag = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        res = 0
        count = 0

        for i in s[::-1]:
            if i in dic:
                res += dic[i] * pow(10, count)
                count += 1
            else:
                return 0

        return res * flag
