"""
author: buppter
datetime: 2019/8/29 13:05


题目描述
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。


解决思路：
动态规划
状态转移方程：s[i] = min(s[t1]*2 , min(s[t2]*3, s[t3]*5))
"""


class Solution:
    def GetUglyNumber_Solution(self, index):
        if index < 7:
            return index

        res = [0] * index
        res[0] = 1
        t2, t3, t5 = 0, 0, 0

        for i in range(1, index):
            res[i] = min(res[t2] * 2, min(res[t3] * 3, res[t5] * 5))
            if res[i] == res[t2] * 2:
                t2 += 1
            if res[i] == res[t3]:
                t3 += 1
            if res[i] == res[t5]:
                t5 += 1

        return res[-1]