#
# Neetcode
# 12. 3 Sum
# Python Solution
#

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # preprocessing: sort input nums in increasing order
        nums = sorted(nums)
        # pick first digit: O(n) outer loop
        # stop iterating 2 digits before end to ensure 2 digits
        # are always available to pair with first digit picked.
        triplets = set()
        for i in range(len(nums) - 2):
            # since the target is 0, we need find the other two numbers
            # to sum up to -nums[i]
            target = -nums[i]
            # two integer sum two pointer algorithm: O(n) inner loop
            # to avoid duplicates, we only search the subarray
            # to the left of i
            j, k = i + 1, len(nums) - 1
            while j < k:
                pair_sum = nums[j] + nums[k]
                if pair_sum == target:
                    triplets.add((nums[i], nums[j], nums[k]))
                    # advance to next triplet
                    k -= 1
                    j += 1
                elif pair_sum > target:
                    # too high: move k towards left to decrease sum
                    k -= 1
                else:
                    # too low: move j towards right to increase sum
                    j += 1
        return [list(x) for x in triplets]
