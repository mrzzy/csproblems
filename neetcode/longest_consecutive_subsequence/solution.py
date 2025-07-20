#
# Neetcode
# 9. Longest Consecutive Subsequence
# Python Solution
#


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen = set(nums)
        # preprocess nums to identify start of sequence
        # start of sequence n are missing n-1 in seen set
        starts = []
        for n in nums:
            if (n - 1) not in seen:
                starts.append(n)

        # extend each start to form unordered subsequence using seen set
        max_len = 0
        for s in starts:
            length = 1
            while (s + 1) in seen:
                s += 1
                length += 1
            max_len = max(max_len, length)
        return max_len
