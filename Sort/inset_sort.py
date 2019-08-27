"""
author: buppter
datetime: 2019/8/27 20:14

插入排序
时间复杂度： O(n*n)
"""


def inset_sort(alist):
    if not alist:
        return None
    for i in range(len(alist) - 1):
        for j in range(1 + i, 0, -1):
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]
            else:
                break
