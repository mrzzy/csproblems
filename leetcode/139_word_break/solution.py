from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """Determine possibility of segmenting 's' using words from 'wordDict'.

        Args:
            s: Target string to segment, truncated by 'end'
            wordDict: List of words that can be used to segment dictionary.
        """
        # cache of target string indexes that has already been segmented.
        # empty target string can always be segmented
        breaks = [True] + [False for _ in range(len(s))]

        # bottom up dp: build up segmentation from empty string
        for i in range(1, len(s) + 1):
            # try out words from word dict
            for word in wordDict:
                begin = i - len(word)
                # reject negative begins as it triggers python's reverse indexing
                if begin < 0:
                    continue
                if s[begin:i] == word and breaks[begin]:
                    # target string s breaks at i
                    breaks[i] = True
                    # skip trying out other words as s[:i] is alreadyh broken
                    break

        return breaks[-1]
