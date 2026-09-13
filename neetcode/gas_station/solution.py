#
# Neetcode
# 72. Gas Station
# Python Solution
#


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # impossible to complete circuit if insufficient gas to complete cost
        if sum(gas) < sum(cost):
            return -1

        start, remaining = 0, 0
        length = len(gas)
        for i in range(length):
            if remaining < 0:
                # insufficient gas to continue
                # start must be reset
                start = i
                remaining = 0
            remaining += gas[i]
            remaining -= cost[i]

        return start
