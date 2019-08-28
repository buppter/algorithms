"""
author: buppter
datetime: 2019/8/28 11:03

归并排序
时间复杂度： O(nlogn)
"""


class MergeSort:
    def merge_sort(self, alist):
        if not alist:
            return None

        n = len(alist)
        if n <= 1:
            return alist

        mid = n // 2

        l_list = self.merge_sort(alist[:mid])
        r_list = self.merge_sort(alist[mid:])
        return self.merge(l_list, r_list)

    def merge(self, l_list, r_list):
        l_point, r_point = 0, 0
        res = []
        while l_point < len(l_list) and r_point < len(r_list):
            if l_list[l_point] < r_list[r_point]:
                res.append(l_list[l_point])
                l_point += 1
            else:
                res.append(r_list[r_point])
                r_point += 1
        res += l_list[l_point:]
        res += r_list[r_point:]
        return res
