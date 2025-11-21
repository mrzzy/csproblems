#
# CSProblems
# EPI
# 6.8 The Look and Say Problem
#

from itertools import groupby

def look_and_say(n: int) -> str:
    if n <= 0:
        raise ValueError("Undefined")
    
   # look and say sequence begins with 1
    seq, next_seq = "1", ""
    for _ in range(1, n):
        # group conditions sequence of characters
        for c, c_seq in groupby(seq):
            next_seq += f"{len(list(c_seq))}{c}"
        seq = next_seq
        next_seq = ""

    return seq

if __name__ == "__main__":
    for i in range(1, 8+1):
        print(f"{i}:", look_and_say(i))
