"""
author: buppter
datetime: 2019/8/21 19:17

题目描述
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.


解决思路：
1. 每次打印第一行，然后矩阵逆时针旋转90度，重复之前步骤(但时间复杂度过高）
2. 具体看代码吧
"""


class Solution1:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if not matrix:
            return []
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix:
                matrix = self.turn(matrix)
        return res

    def turn(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        res = []

        for i in range(cols - 1, -1, -1):
            new_res = []
            for j in range(rows):
                new_res.append(matrix[j][i])

            res.append(new_res)
        return res


class Solution2:
    def __init__(self):
        self.res = []

    def printMatrix(self, matrix):

        if not matrix:
            return self.res

        row = len(matrix)
        col = len(matrix[0])

        if not row or not col:
            return self.res

        elif row == 1:
            self.res += matrix[0]
            return self.res

        for i in range(col):
            self.res.append(matrix[0][i])
        for i in range(1, row):
            self.res.append(matrix[i][col - 1])
        if row > 1:
            for i in range(col - 2, -1, -1):
                self.res.append(matrix[row - 1][i])
        if col > 1:
            for i in range(row - 2, 0, -1):
                self.res.append(matrix[i][0])

        new_matrix = [l[1: col - 1] for l in matrix[1: row - 1]]
        if new_matrix:
            self.printMatrix(new_matrix)
        return self.res
