#
# CSProblems
# Neetcode
# NC6. Encode and Decode Strings
#

class Solution:
    def encode(self, strs: List[str]) -> str:
        # run length encoding: each string s in strs is encoded as:
        # "<length of s>\0s"
        return "".join([f"{len(s)}\0{s}" for s in strs])

    def decode(self, s: str) -> List[str]:
        strs = []
        # j pointer tracks "already parsed"
        j = 0
        for i, c in enumerate(s):
            print(c)
            if c == "\0":
                # parse length of substring
                s_len = int(s[j:i])
                # extract substring by parsed length
                s_end = i + 1 + s_len
                strs.append(s[i + 1 : s_end])
                j = s_end

        return strs
