from string import ascii_lowercase


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagram groups: key: tuple of character counts
        groups = {}
        # index characters relative to base character 'a'
        base = ord("a")
        for s in strs:
            counts = [0] * len(ascii_lowercase)
            for c in s:
                # compute index of character c, relative to base character 'a'
                counts[ord(c) - base] += 1

            # add string s to anagram group with same character counts
            key = tuple(counts)
            if key not in groups:
                groups[key] = []
            groups[key].append(s)

        return list(groups.values())
