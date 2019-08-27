"""
author: buppter
datetime: 2019/8/27 14:08

快排
时间复杂度： O(nlogn)
"""


def quick_sort(alist, start, end):
    if not alist:
        return None
    if start > end:
        return
    low = start
    high = end
    mid = alist[start]

    while low < high:
        while low < high and alist[high] > mid:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid:
            low += 1
        alist[high] = alist[low]

    alist[low] = mid

    quick_sort(alist, start, low - 1)
    quick_sort(alist, low + 1, end)
