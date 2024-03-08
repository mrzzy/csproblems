#
# Leetcode
# 76. Minimum Window Substring
#

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # count characters in t
        t_counts = Counter(t)

        # tabulate the balance of characters required in the substring
        substr_balance = {c: -v for c, v in t_counts.items()}
        min_substr = None
        i, j = 0, 0

        # add first character
        if s[i] in substr_balance:
            substr_balance[s[i]] += 1

        while True:
            # check if substr contains characters in t
            if all(b >= 0 for b in substr_balance.values()):
                if min_substr is None or j - i + 1 < len(min_substr):
                    # found new min substr
                    min_substr = s[i : j + 1]
                # contract substr to find smaller substr
                if s[i] in substr_balance:
                    substr_balance[s[i]] -= 1
                i += 1
            else:
                if j + 1 >= len(s):
                    break
                # expand substr to fulfill t character requirement
                j += 1
                if s[j] in substr_balance:
                    substr_balance[s[j]] += 1

        return "" if min_substr is None else min_substr
