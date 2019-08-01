"""
author: buppter
datetime: 2019/7/31 12:34

题目描述：
实时判断数据流中第K大的数
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order,
not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums,
which contains initial elements from the stream. For each call to the method KthLargest.add, return the
element representing the kth largest element in the stream.

示例：
int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8

解题思路：
使用优先队列
"""


# 第一种方法，使用了 堆 ，但是会超时
from heapq import heapify, nlargest, heappush
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapify(nums)
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        heappush(self.nums, val)
        largest = nlargest(self.k, self.nums)
        return largest.pop()


# 第二种方法
import bisect


class _KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        bisect.insort(self.nums, val)
        return self.nums[len(self.nums) - self.k]
