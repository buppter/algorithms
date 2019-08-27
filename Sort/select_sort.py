"""
author: buppter
datetime: 2019/8/27 20:05

选择排序
时间复杂度： O(n*n)
"""


def select_sort(alist):
    if not alist:
        return None
    for i in range(len(alist)):
        min_index = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[min_index]:
                min_index = j

        if min_index != i:
            alist[i], alist[min_index] = alist[min_index], alist[i]

