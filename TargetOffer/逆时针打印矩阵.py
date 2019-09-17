"""
author: buppter
datetime: 2019/9/17 15:27


顺时针打印矩阵的变形，这次进行逆时针打印
"""


class Solution1:
    def __init__(self):
        self.res = []

    def printMatrix(self, matrix):
        if not matrix:
            return self.res

        row = len(matrix)
        col = len(matrix[0])

        if not row or not col:
            return self.res

        if row == 1:
            self.res += matrix[0]
            return self.res

        for i in range(row):
            self.res.append(matrix[i][0])

        for i in range(1, col):
            self.res.append(matrix[row - 1][i])
        if col > 1:
            for i in range(row - 2, -1, -1):
                self.res.append(matrix[i][col - 1])

        for i in range(col - 2, 0, -1):
            self.res.append(matrix[0][i])

        new_matrix = [l[1: col - 1] for l in matrix[1: row - 1]]
        if new_matrix:
            self.printMatrix(new_matrix)
        return self.res


class Solution2:
    def printMatrix(self, matrix):
        res = []
        while matrix:

            if matrix and matrix:
                for i in matrix:
                    res.append(i.pop(0))

            if matrix and matrix[0]:
                res += matrix.pop()
            if matrix and matrix[0]:
                for i in matrix[::-1]:
                    res.append(i.pop())
            if matrix and matrix[0]:
                res += matrix.pop(0)[::-1]

            if len(matrix[0]) == 0:
                break
        return res
