"""
author: buppter
datetime: 2019/8/12 12:30

题目描述：
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.


示例：
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1
"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        res = [amount + 1] * (amount + 1)
        res[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i >=c:
                    res[i] = min(res[i], res[i - c] + 1)
        if res[amount] == amount + 1:
            return -1
        return res[amount]

