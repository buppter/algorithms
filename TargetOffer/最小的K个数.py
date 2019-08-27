"""
author: buppter
datetime: 2019/8/14 16:14


题目描述
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

解决思路：
1. 排序返回前4个数
2. 建立大顶堆
3. 快排思想
"""


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput or k > len(tinput):
            return []
        tinput.sort()
        return tinput[:k]


class Solution2:
    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput or k > len(tinput) or not k:
            return []
        start = 0
        end = len(tinput) - 1
        s = self.quick_sort(tinput, start, end)
        while s + 1 != k:
            if s + 1 > k:
                end = s - 1
            if s + 1 < k:
                start = s + 1
            s = self.quick_sort(tinput, start, end)

        return tinput[:k]

    def quick_sort(self, alist, start, end):
        if start > end:
            return
        low = start
        high = end
        mid = alist[start]

        while low < high:
            while alist[high] >= mid and low < high:
                high -= 1
            alist[low] = alist[high]
            while alist[low] < mid and low < high:
                low += 1
            alist[high] = alist[low]
        alist[low] = mid
        return low


class Solution3:
    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput or not k or k > len(tinput):
            return []

        heap_k = tinput[:k]
        self.build_heap(heap_k, k)

        for i in tinput[k:]:
            if i < heap_k[0]:
                heap_k[0] = i
                self.heapify(heap_k, k, 0)
        return heap_k

    def build_heap(self, alist, length):
        last_node_index = length - 1
        last_node_parent_index = (last_node_index - 1) // 2
        for i in range(last_node_parent_index, -1, -1):
            self.heapify(alist, length, i)

    def heapify(self, alist, length, i):
        if i > length:
            return

        max_index = i
        l_node_index = 2 * i + 1
        r_node_index = 2 * i + 2
        if l_node_index < length and alist[l_node_index] > alist[max_index]:
            max_index = l_node_index
        if r_node_index < length and alist[r_node_index] > alist[max_index]:
            max_index = r_node_index

        if max_index != i:
            alist[i], alist[max_index] = alist[max_index], alist[i]
            self.heapify(alist, length, max_index)
