#
# Neetcode
# 84. Best Time to Buy and Sell Stock with Cooldown
# Python Solution
#


from functools import cache

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        @cache
        def _maxProfit(i: int, j: int) -> int:
            if i >= j:
                # not enough time to make a profit
                return 0

            # iterate selling times
            max_profit = _maxProfit(i+1, j)
            for s in range(i+1, j):
                # buy at i, sell at s, cooldown + 2 day
                profit = prices[s] - prices[i] + _maxProfit(s+2, j)
                max_profit = max(max_profit,  profit)
            
            return max_profit
        
        return _maxProfit(0, len(prices))
