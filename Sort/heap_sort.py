"""
author: buppter
datetime: 2019/8/27 13:45

堆排序
时间复杂度： O(nlogn)
"""


class HeapSort:
    def heap_sort(self, alist, length):
        if not alist or not length:
            return None

        self.build_heap(alist, length)

        for i in range(length - 1, 0, -1):
            alist[i], alist[0] = alist[0], alist[i]
            self.heapify(alist, i, 0)

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
