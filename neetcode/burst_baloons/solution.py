#
# Neetcode
# 83. Burst Balloons
# Python Solution
#


class Solution:
    def __init__(self):
        self.cache = {}
        
    def maxCoins(self, nums: list[int]) -> int:
        # pad with 1s
        nums = [1] + nums + [1]
        return self.max_coins(nums, 1, len(nums) - 1)

    def max_coins(self, nums: list[int], i: int, j: int) -> int:
        """Finds the max coins solution for nums[i:j]"""
        # DP: used cached solution if any
        key = (i, j)
        if key in self.cache:
            return self.cache[key]
        
        # try out different popping positions
        best = 0
        for p in range(i, j):
            # recursively explore the most coins that be be attained
            # by popping other balloons
            coins = self.max_coins(nums, i, p)
            coins += self.max_coins(nums, p+1, j)

            # compute score attained by popping balloon p last
            coins += nums[i-1] * nums[p] * nums[j]

            best = max(best, coins)

        self.cache[key] = best
        return best
