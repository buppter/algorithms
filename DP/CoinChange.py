"""
author: buppter
datetime: 2019/8/28 13:21

硬币兑换问题
状态转移方程： dp[i] = min{dp[i - coin_1] + 1, dp[i - coin_2] + 1, dp[i - coin] + 1}
"""


def coin_change(coins, amount):
    if not coins:
        return -1

    res = [float('inf')] * (amount + 1)
    res[0] = 0

    for i in range(1, amount + 1):
        min_coins = res[i]
        for coin in coins:
            if i - coins >= 0:
                min_coins = min(res[i - coin] + 1, min_coins)
        res[i] = min_coins

    if res[amount] != float('inf'):
        return res[amount]
    return -1
