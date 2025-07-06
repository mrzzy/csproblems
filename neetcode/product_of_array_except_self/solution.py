#
# CSProblems
# Neetcode
# NC7. Products of Array Except Self
#


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # precompute prefix products
        prefix = [1]
        for n in nums:
            prefix.append(prefix[-1] * n)

        # precompute suffix products
        suffix = [1]
        for n in reversed(nums):
            suffix.append(suffix[-1] * n)

        # compute products
        products = []
        for i in range(len(nums)):
            products.append(prefix[i] * suffix[-i - 2])
        return products
