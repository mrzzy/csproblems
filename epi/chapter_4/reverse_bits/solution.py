#
# CSProblems
# Elements of Programming Interviews
# 4.3 Reverse Bits
#

# Task: reverse bits in 64-bit word


def reverse_bits(word: int, n_bits: int) -> int:
    for i in range(0, n_bits // 2):
        j = n_bits - 1 - i
        i_mask, j_mask = (1 << i), (1 << j)

        if (word & i_mask > 0) == (word & j_mask > 0):
            # bits identical, no need to swap
            continue
        # swap bits by flipping them with xor
        flip_mask = i_mask | j_mask
        word ^= flip_mask
    return word


def reverse_cache(word: int, n_bits: int, n_cache: int = 16):
    # precompute n_cache bit mask
    cache = {}
    mask = (1 << n_cache) - 1
    for i in range(mask + 1):
        cache[i] = reverse_bits(i, n_cache)
    reverse = 0
    # lookup precomputed results in reverse to form reversed bits
    for i in range(n_bits // n_cache - 1, -1, -1):
        reverse |= cache[word & mask] << (i * n_cache)
        word >>= n_cache
    return reverse


if __name__ == "__main__":
    print(bin(reverse_bits(0b01101011, 8)))
    print(bin(reverse_cache(0b01101011, 8, 2)))
