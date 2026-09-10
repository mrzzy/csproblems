#
# Neetcode
# 68. Jump Game
# Python Solution
#


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # bottom up dp
        # init base cases
        is_jumpable = [False for _ in range(len(nums))]
        # end state is always jumpable from end state
        is_jumpable[-1] = True

        for i in range(len(nums) - 1, -1, -1):
            # iterate number of jumps from i
            for j in range(1, nums[i] + 1):
                jump_to = i + j
                if jump_to < len(nums):
                    is_jumpable[i] = is_jumpable[i] or is_jumpable[jump_to]

        return is_jumpable[0]
