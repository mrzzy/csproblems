#
# CS Problems
# Leetcode
# 39. Combination Sum
#

from typing import List, Tuple


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # stack of sums to process
        combinations = set()
        # (combination, remaining, candidate offset)
        sums = [([], target, 0)]  # type: List[Tuple[List[int], int, int]]

        while len(sums) > 0:
            combination, remaining, offset = sums.pop()
            if remaining == 0:
                # record combination to that forms target value
                combinations.add(tuple(sorted(combination)))
            else:
                # permutate possible sum combinations with candidate digits
                for digit in candidates[offset:]:
                    if remaining - digit >= 0:
                        next_combination = combination[:]
                        next_combination.append(digit)
                        next_offset = offset
                        if (
                            len(combination) > 0
                            and digit != combination[-1]
                            and offset + 1 < len(candidates)
                        ):
                            next_offset = offset + 1
                        sums.append((next_combination, remaining - digit, next_offset))

        return list(combinations)
