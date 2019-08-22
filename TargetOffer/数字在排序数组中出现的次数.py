"""
author: buppter
datetime: 2019/8/15 15:05

题目描述
统计一个数字在排序数组中出现的次数。
"""


class Solution:
    def GetNumberOfK1(self, data, k):
        # write code here
        if not data or not k:
            return 0
        return data.count(k)

    def GetNumberOfK2(self, data, k):
        if not data or not k:
            return 0
        count = 0
        for i in data:
            if i == k:
                count += 1
        return count

    def GetNumberOfK3(self, data, k):
        if not data or not k:
            return 0
        if k not in data:
            return 0
        l = 0
        r = len(data) - 1

        while data[l] != k and l < r:
            l += 1
        while data[r] != k and l < r:
            r -= 1
        return r - l + 1

    # 二分查找
    def GetNumberOfK4(self, data, k):
        if not data:
            return 0

        low = self.binary_search(data, k - 0.5)
        high = self.binary_search(data, k + 0.5)
        return high - low

    def binary_search(self, data, k):
        low = 0
        high = len(data) - 1
        while low <= high:
            mid = (low + high) // 2
            if data[mid] > k:
                high = mid - 1
            else:
                low = mid + 1
        return low


if __name__ == "__main__":
    s = Solution()
    res = s.GetNumberOfK4([3,3,3,3,4,5],3)
    print(res)
