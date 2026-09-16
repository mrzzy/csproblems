#
# Neetcode
# 86. Edit Distance
# Python Solution
#

from functools import cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.distance(word1, word2, 0, 0)

    @cache
    def distance(self, word1: str, word2: str, i: int, j: int) -> int:
        """Computes min edit distance.

        Args:
            i: Index of word 1
            j: Index of word 2
        """
        # base cases: either word is empty
        # delete all other letters in the other word
        w1_remaining = len(word1) - i
        w2_remaining = len(word2) - j

        if w1_remaining <= 0:
            return w2_remaining
        if w2_remaining <= 0:
            return w1_remaining

        # recursively search for min edit distance
        replace_cost = word1[i] != word2[j]
        min_edit = min(
            self.distance(word1, word2, i + 1, j + 1) + replace_cost,
            self.distance(word1, word2, i + 1, j) + 1,
            self.distance(word1, word2, i, j + 1) + 1,
        )
        return min_edit
