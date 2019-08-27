"""
author: buppter
datetime: 2019/8/27 14:46

二分查找
"""


def binary_search1(alist, target):
    """
    迭代版本
    :param alist: 待查找数组
    :param target: 目标数字
    :return: 如果存在返回下标，否则返回 -1
    """
    if not alist or not target:
        return False
    start = 0
    end = len(alist) - 1

    while start <= end:
        mid = (start + end) // 2

        if alist[mid] == target:
            return True
        elif alist[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False


def binary_search2(alist, target):
    """
    递归版本
    """
    if not alist or not target:
        return False

    lens = len(alist)

    if lens > 0:
        mid = lens // 2

        if alist[mid] == target:
            return True
        elif alist[mid] > target:
            return binary_search2(alist[:mid], target)
        else:
            return binary_search2(alist[mid + 1:], target)
    return True
