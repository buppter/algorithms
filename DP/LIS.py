"""
author: buppter
datetime: 2019/8/28 15:32

最长非降子序列

状态转移方程： d[i] = max(1, d[j] + 1)
j < i, alist[j] <= alist[i]
"""


def LIS(alist):
    if not alist:
        return 0

    res = [1] * len(alist)
    for i in range(1, len(alist)):
        for j in range(i):
            if alist[j] < alist[i]:
                res[i] = max(res[i], res[j] + 1)
    return max(res)