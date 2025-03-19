#
# CSProblems
# Elements of Programming Interviews
# 4.2 Swap bits
#

# Task: swap bits in the ith and jth positions

def swap_bits(word: int, i: int, j: int) -> int:
    if word & (1 << i) == word & (1 << j):
        # bits are the same, no swap is necessary
        return word

    # swap: effectively flips ith and jth bit, swap can be performed via xor
    flip_mask = (1 << i) | (1 << j)
    return word ^ flip_mask

if __name__ == '__main__':
    print(bin(swap_bits(0b01011001, 0, 7)))
