#
# Neetcode
# 11. Two Integer Sum
# Python Solution
#

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            two_sum = numbers[i] + numbers[j]
            if two_sum == target:
                # found pair matching target sum
                # + 1 for 1 indexing
                return [i + 1, j + 1]
            elif two_sum < target:
                # target sum is too low:
                # advance i to the right to increase total sum
                # since elements are in increasing order
                i += 1
            elif two_sum > target:
                # target sum is too high:
                # advance j to the left to reduce total sum
                # since elements are in decreasing order
                j -= 1
        raise ValueError("No solution found")
