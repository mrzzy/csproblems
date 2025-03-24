#
# CSProblems
# Elements of Programming Interviews
# 4.4 Closest Int with Same Weight
#

# task: return int with same weight (same no. of bits set) with minimal difference
# as given integer n


def closet_int(n: int, n_bits: int = 64):
    for i in range(n_bits):
        # find the lsbs that differ
        first_mask, second_mask = (1 << i), (1 << (i + 1))
        if ((n & first_mask) == 0) != ((n & second_mask) == 0):
            # swap bits i and i+1
            # 0x3: 11 in binary
            flip_mask = first_mask | second_mask
            return n ^ flip_mask
    raise RuntimeError("No such integer exists")


if __name__ == "__main__":
    print(closet_int(6))
    print(closet_int(4))
    print(closet_int(7))
    print(closet_int(11))
