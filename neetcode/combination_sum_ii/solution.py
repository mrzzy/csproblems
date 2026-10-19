#
# Neetcode
# 96. Combination Sum II
# Python Solution
#

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates = sorted(candidates)
        combinations = []  # type: list[list[int]]

        def combine(i: int, sum_seq: list[int], sum_value: int):
            # base case: no more candidates to consider
            if i >= len(candidates):
                if sum_value == target:
                    # make a copy of sum sequence since we will admend
                    # the copy when backtracking later
                    combinations.append(sum_seq.copy())
                return

            candidate = candidates[i]

            # recursive cases
            if sum_value + candidate <= target:
                # select candidate at position as part of sum
                sum_seq.append(candidate)
                combine(i + 1, sum_seq, sum_value + candidate)
                # backtrack decision by removing candidate from sum
                sum_seq.pop()
            # skip candidate at position as part of sum
            # skip duplicates with same value as candidate
            # sorting should have brought all duplicate values together
            j = 0
            while i + j < len(candidates) and candidates[i + j] == candidate:
                j += 1
            combine(i + j, sum_seq, sum_value)

        combine(0, [], 0)
        return combinations
