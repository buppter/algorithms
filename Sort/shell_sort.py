"""
author: buppter
datetime: 2019/8/27 20:56

希尔排序
时间复杂度： O(nlogn)
"""


def shell_sort(alist):
    if not alist:
        return None

    gap = len(alist) // 2
    while gap > 0:
        for i in range(gap, len(alist)):
            j = i
            while j >= gap and alist[j - gap] > alist[j]:
                alist[j - gap], alist[j] = alist[j], alist[j - gap]

                j -= gap
        gap //= 2


alist = [54, 226, 93, 17, 77, 31, 44, 55, 20]
shell_sort(alist)
print(alist)
