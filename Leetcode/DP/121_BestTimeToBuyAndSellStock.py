"""
author: buppter
datetime: 2019/8/11 15:35

题目描述：
最佳股票买卖时间
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one


示例：
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


解题思路：

"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        minP = prices[0]
        res = [0 for _ in range(len(prices))]
        for i in range(1, len(prices)):
            if prices[i] < minP:
                minP = prices[i]
            else:
                res[i] = prices[i] - minP
        return max(res)


if __name__ == "__main__":
    s = Solution()
    prices = [7,1,5,3,6,4]
    res = s.maxProfit(prices)
    print(res)
