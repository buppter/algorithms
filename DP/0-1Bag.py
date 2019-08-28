"""
author: buppter
datetime: 2019/8/28 14:08

0-1 背包问题

状态转义方程： bag[i][j] = max{
                                0,                                          i == 0 or j ==  0
                                bag[i - 1][j],                             weight[i] > j
                                value[i] + bag[i - 1][j - weight[i]],    weight[i] <= j
                                }
i 表示每一个物品
j 表示每个重量的背包（子问题）
"""


class Bag01:
    def bag01(self, weight, value, max_weight):
        """
        :param weight: 物品重量
        :param value: 物品价值
        :param max_weight:  背包最大重量
        :return: 最大价值
        """
        res = [[0 for _ in range(max_weight + 1)] for _ in range(len(weight) + 1)]

        for i in range(1, len(res)):  # 每个物品
            cur_value = value[i - 1]
            cur_weight = weight[i - 1]
            for j in range(1, len(res[0])):  # 每个重量的背包
                if cur_weight <= j:
                    res[i][j] = max(res[i - 1][j], cur_value + res[i - 1][j - cur_weight])
                else:
                    res[i][j] = res[i - 1][j]

        r_index = self.show(res, weight)

        return res[-1][-1], r_index

    def show(self, res, weight):
        """
        装入背包的物品索引(索引从0开始）
        :param res:
        :param weight:
        :return: 返回物品索引
        """
        r = []
        j = len(res[0]) - 1
        for i in range(len(res) - 1, 0, -1):
            if res[i][j] > res[i - 1][j]:
                r.append(i - 1)
                j -= weight[i - 1]
        return r


if __name__ == '__main__':
    weight = [2, 2, 3, 1, 5, 2]
    value = [2, 3, 1, 5, 4, 3]
    max_weight = 10
    s = Bag01()
    res, r_index = s.bag01(weight, value, max_weight)
    print(res)
    print(r_index)
