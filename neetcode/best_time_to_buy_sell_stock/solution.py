#
# Neetcode
# 15. Best Time to Buy Sell Stock
# Python Solution
#


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit, max_price = 0, 0
        for price in reversed(prices):
            # calculate profit of buying at current selling at max_price
            profit = max_price - price
            # track max profit & price
            max_profit = max(max_profit, profit)
            max_price = max(max_price, price)
        return max_profit
