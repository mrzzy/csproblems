#
# Neetcode
# 74. Alien Dictionary
# Python Solution
#


from collections import defaultdict


class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        dependencies = defaultdict(list)
        chars = set()

        for word in words:
            for c in word:
                chars.add(c)
        # parse words for lexical dependencies
        for i in range(len(words) - 1):
            # compare pairwise words for differences
            left, right = words[i], words[i + 1]
            for j in range(min(len(left), len(right))):
                if left[j] != right[j]:
                    # 1st letter differ is smaller
                    # lexical dependency: longer[j] -> smaller[j]
                    dependencies[right[j]].append(left[j])
                    break
            else:
                # left must be a prefix of right, or no order possible
                if len(left) > len(right):
                    return ""

        order, completed, seen = [], set(), set()
        for c in chars:
            # dfs to produce lexical order of elements
            def dfs(c: str) -> bool:
                if c in seen:
                    # no lexical ordering possible
                    return False

                if c in completed:
                    # skip already completed
                    return True

                seen.add(c)
                # output dependencies first
                for d in dependencies[c]:
                    if not dfs(d):
                        # no ordering possible
                        return False

                # output current char
                order.append(c)
                completed.add(c)

                seen.remove(c)
                return True

            if not dfs(c):
                order = []

        return "".join(order)
