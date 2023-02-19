#
# CSProblems
# Leetcode
# 20. Valid Parentheses
#


class Solution:
    def isValid(self, s):
        """
        Determine if the given string of brace characters is valid.
        Validity is defined by the string having matching opening & closing brance characters.
        :type s: str
        :rtype: bool
        """

        def invert(brace: str) -> str:
            if brace == "]":
                return "["
            if brace == ")":
                return "("
            if brace == "}":
                return "{"
            raise ValueError(f"Unsupported: {brace}")

        open_braces = []
        for c in s:
            if c in {"[", "(", "{"}:
                # add to open braces stack
                open_braces.append(c)
            if c in {"]", ")", "}"}:
                if len(open_braces) <= 0:
                    # no open braces for closing brace
                    return False
                # pop & expect matching of the open braces
                open_brace = open_braces.pop()
                if invert(c) != open_brace:
                    return False
        # check all open braces are closed
        return len(open_braces) <= 0
