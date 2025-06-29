#
# Neetcode
# NC3. Two sum
#


from collections import deque


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # build reverse index of num -> index
        index = {}
        for i, num in enumerate(nums):
            if num not in index:
                index[num] = deque()
            index[num].append(i)

        for i, num in enumerate(nums):
            # remove i from index for num to prevent duplicate pairings
            index[num].popleft()

            # expected pair sum can be computed from target
            expected = target - num
            if expected in index and len(index[expected]) > 0:
                j = index[expected][0]
                if j < i:
                    # swap i, j to ensure that smaller index comes first
                    i, j = j, i
                return [i, j]
        else:
            raise ValueError("Expected at least number pair to form target sum.")
