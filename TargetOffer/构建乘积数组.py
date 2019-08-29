"""
author: buppter
datetime: 2019/8/29 14:52


题目描述
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
不能使用除法。


解决思路：
新数组B中的成员B[i]是A中不包含A[i]的所有元素乘积；
即 B[0] = A[1] * A[2] * ... * A[n - 1]
"""


class Solution:
    def multiply(self, A):
        if not A:
            return []

        B = [0] * len(A)
        B[0] = 1
        for i in range(1, len(A)):
            B[i] = B[i - 1] * A[i - 1]

        tmp = 1
        for i in range(len(A) - 2, -1, -1):
            tmp *= A[i + 1]
            B[i] *= tmp
        return B
