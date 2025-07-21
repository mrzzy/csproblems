#
# Neetcode
# 10. Valid Palindrome
# Python Solution
#

import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # filter out unchecked characters
        check_set = set(string.ascii_letters + string.digits)
        s = "".join(c for c in s if c in check_set)
        # characters sampled from both ends by 2 pointers i, j
        # should match in palindrome
        i, j = 0, len(s) - 1
        while i < j:
            if s[i].lower() != s[j].lower():
                return False
            # ok: advance to next character
            i += 1
            j -= 1

        return True
