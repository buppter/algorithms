"""
author: buppter
datetime: 2019/8/14 16:01

题目描述
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。


解决思路：
1. 排序，找到中位数，判断中位数的次数是否超过数组长度的一半，时间复杂度O(nlogn)，不是最优
2. 在遍历数组时保存两个值：一是数组中一个数字，一是次数。遍历下一个数字时，若它与之前保存的数字相同，则次数加1，否则次数减1；
若次数为0，则保存下一个数字，并将次数置为1。遍历结束后，所保存的数字即为所求。然后再判断它是否符合条件即可。时间复杂度O(n)
3. 统计数字的次数
"""


class Solution:
    def MoreThanHalfNum_Solution1(self, numbers):
        if not numbers:
            return 0
        size = len(numbers)
        numbers.sort()
        res = numbers[size // 2]

        count = numbers.count(res)
        if count > size // 2:
            return res
        return 0

    def MoreThanHalfNum_Solution2(self, numbers):
        if not numbers:
            return 0

        num = numbers[0]
        count = 1
        for i in numbers[1:]:
            if i == num:
                count += 1
            else:
                count -= 1

            if count == 0:
                num = i
                count = 1

        c = 0

        for i in numbers:
            if num == i:
                c += 1
        if c > len(numbers) // 2:
            return num
        return 0

    def MoreThanHalfNum_Solution3(self, numbers):
        if not numbers:
            return 0
        size = len(numbers)
        res = {}
        for i in numbers:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        for k, v in res.items():
            if v > size // 2:
                return k
        return 0
