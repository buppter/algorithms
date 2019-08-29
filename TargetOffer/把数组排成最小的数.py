"""
author: buppter
datetime: 2019/8/29 13:59


题目描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。


解决思路：
先将整型数组转换成String数组，然后将String数组排序，最后将排好序的字符串数组拼接出来。关键就是制定排序规则。
排序规则如下：
若ab > ba 则 a > b，
若ab < ba 则 a < b，
若ab = ba 则 a = b；
解释说明：
比如 "3" < "31"但是 "331" > "313"，所以要将二者拼接起来进行比较
"""
import functools


class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ''

        res = list(map(str, numbers))
        res.sort(key=functools.cmp_to_key(self.compare))
        return ''.join(res)

    def compare(self, s1, s2):
        num1 = s1 + s2
        num2 = s2 + s1
        if num1 < num2:
            return -1
        elif num1 > num2:
            return 1
        else:
            return 0
