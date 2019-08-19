"""
author: buppter
datetime: 2019/8/19 13:02

题目描述
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
"""


class Solution:
    def __init__(self):
        self.count = 0

    def movingCount(self, threshold, rows, cols):
        arr = [[1 for i in range(cols)] for j in range(rows)]
        self.find(arr, 0, 0, threshold)
        return self.count

    def find(self, arr, i, j, threshold):
        if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0]):
            return

        tmpi = list(map(int, list(str(i))))
        tmpj = list(map(int, list(str(j))))
        if sum(tmpi) + sum(tmpj) > threshold or arr[i][j] != 1:
            return
        arr[i][j] = 0
        self.count += 1
        self.find(arr, i + 1, j, threshold)
        self.find(arr, i - 1, j, threshold)
        self.find(arr, i, j + 1, threshold)
        self.find(arr, i, j - 1, threshold)
