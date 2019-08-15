"""
author: buppter
datetime: 2019/8/15 16:20

题目描述
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。


解决思路：
1. 遍历
2. 位运算：两个相同数字异或=0，一个数和0异或还是它本身。
"""


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if not array:
            return []
        res = []
        for i in array:
            if i not in res:
                res.append(i)
            else:
                res.remove(i)
        return res
