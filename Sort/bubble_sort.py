"""
author: buppter
datetime: 2019/8/27 19:33

冒泡排序
时间复杂度： O(n*n)
"""


def bubble_sort(alist):
    if not alist:
        return None

    for i in range(len(alist)):
        for j in range(len(alist) - 1 - i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
