"""
author: buppter
datetime: 2019/9/1 12:38


解决思路：
假设第 i 中物品放入背包的数量是 k，那么 k 必须满足：
     0 <= k <= max_weight // weight[i]

因此转移方程为：

res[i][j] = max( res[i - 1][j - weight[i] * k])  0 <= k <= max_weight // weight[i]
"""


class Solution:

    def comp_bag(self, weight, value, max_weight):
        if not weight or not value or not max_weight:
            return 0

        res = [0 for _ in range(max_weight + 1)]

        for i in range(1, len(weight) + 1):
            for j in range(1, max_weight + 1):
                if j >= weight[i - 1]:
                    res[j] = max(res[j], res[j - weight[i - 1]] + value[i - 1])
        return res[-1]
