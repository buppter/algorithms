"""
author: buppter
datetime: 2019/9/1 12:38


解决思路：
多重背包问题，即每种物品有一定的数量，这时候可以转换成01背包问题
例如：第i种物品有三个，可以把这三个物品看成重量和价值相同的三个物品，从而转换为01背包问题
"""


class Solution1:
    def multiple_bag(self, weight_list, value_list, num_list, max_weight):
        """
        多重背包
        :param weight_list: 物品重量
        :param value_list: 物品对应的价值
        :param num_list: 物品对应的数量
        :param max_weight: 背包最大重量
        :return: 背包所装物品的最大价值
        """
        if not weight_list or not value_list or not num_list or not max_weight:
            return 0
        weight, value = self.turn(weight_list, value_list, num_list)
        res = self.bag01(weight, value, max_weight)
        return res

    def bag01(self, weight, value, max_weight):
        res = [0 for _ in range(max_weight + 1)]

        for i in range(1, len(weight) + 1):
            for j in range(max_weight, 0, -1):
                if j >= weight[i - 1]:
                    res[j] = max(res[j], res[j - weight[i - 1]] + value[i - 1])
        return res[-1]

    def bag01_2(self, weight, value, max_weight):
        res = [[0 for _ in range(max_weight + 1)] for _ in range(len(weight) + 1)]

        for i in range(1, len(res)):  # 每个物品
            cur_value = value[i - 1]
            cur_weight = weight[i - 1]
            for j in range(1, len(res[0])):  # 每个重量的背包
                if cur_weight <= j:
                    res[i][j] = max(res[i - 1][j], cur_value + res[i - 1][j - cur_weight])
                else:
                    res[i][j] = res[i - 1][j]
        return res[-1][-1]

    def turn(self, weight_list, value_list, num_list):
        """
        讲物品转换为01背包的物品
        """
        weight = []
        value = []

        for i in range(len(weight_list)):
            for j in range(num_list[i]):
                weight.append(weight_list[i])
                value.append(value_list[i])

        return weight, value


class Solution2:
    """
    Solution1 的物品拆分方法会增加时间复杂度和空间复杂度，可以使用二进制分解进行代码优化
    """

    def multi_bag(self, weight_list, value_list, num_list, max_weight):
        if not weight_list or not value_list or not num_list or not max_weight:
            return 0

        weight, value = self.turn(weight_list, value_list, num_list)
        res = self.bag01(weight, value, max_weight)
        return res

    def bag01(self, weight, value, max_weight):
        res = [0 for _ in range(max_weight + 1)]

        for i in range(1, len(weight) + 1):
            for j in range(max_weight, 0, -1):
                if j >= weight[i - 1]:
                    res[j] = max(res[j], res[j - weight[i - 1]] + value[i - 1])
        return res[-1]

    def turn(self, weight_list, value_list, num_list):
        weight = []
        value = []
        for i in range(len(weight_list)):
            for j in self.binary_decomposition(num_list[i]):
                weight.append(weight_list[i] * j)
                value.append(value_list[i] * j)
        return weight, value

    def binary_decomposition(self, n):
        k = 0
        res = []
        while n - pow(2, k + 1) + 1 > 0:
            res.append(pow(2, k))
            k += 1
        res.append(n - pow(2, k) + 1)
        return res


if __name__ == '__main__':
    weight_list = [2, 2, 1]
    value_list = [20, 10, 6]
    num_list = [2, 5, 10]
    max_weight = 8

    s1 = Solution1()
    res = s1.multiple_bag(weight_list, value_list, num_list, max_weight)
    print(res)

    s2 = Solution2()
    res = s2.multi_bag(weight_list, value_list, num_list, max_weight)
    print(res)
