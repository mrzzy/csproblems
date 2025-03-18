#
# CSProblems
# Elements of Programming Interviews
# 4.1 Computing Parity of a Word
#

# Task: Compute parity of 64-bit word.
# Return 0 for even parity 1 for odd parity


def parity_brute_force(word: int) -> int:
    # O(n)
    n_set = 0
    for i in range(64):
        # get lowermost bit
        n_set += word & 1
        # shift bits right, discarding least siginifcant bit
        word = word >> 1
    return n_set % 2


def parity_set_only(word: int) -> int:
    # O(k) where k is the set no. of bits
    n_set = 0
    for i in range(64):
        # get last set bit
        n_set += word & ~(word - 1)
        # erase last set bit
        word &= word - 1

    return n_set % 2


def parity_cache(word: int) -> int:
    # precompute cache for 16 bit words
    n_cache = 16
    cache = {}
    for w in range(0xFF):
        cache[w] = parity_set_only(w)

    parity = 0
    for i in range(64 // n_cache):
        # bring down and extract the ith 16bit word
        # ^ combines parity of sub words
        parity ^= cache[(word >> i) & 0xFF]

    return parity


def parity_divide_conquer(word: int, n_bits: int = 64):
    if n_bits <= 0:
        return 0
    if n_bits == 1:
        return word & 1

    # divide and conquer: divide into 2 sub words, compute sub word parity and combine into final result
    n_half = n_bits // 2
    n_half_mask = (1 << n_half) - 1

    return parity_divide_conquer(word & n_half_mask, n_half) ^ parity_divide_conquer(
        (word >> n_half) & n_half_mask, n_half
    )


if __name__ == "__main__":
    print(parity_brute_force(0xFD))
    print(parity_set_only(0xFD))
    print(parity_cache(0xFD))
    print(parity_divide_conquer(0xFD))
