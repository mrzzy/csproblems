#
# CSProblems
# Elements of Programming Interviews
# 5.12 Sample Offline Data
#

from random import randint


def sample(array: list[int], n_subset: int) -> list[int]:
    # iterate elements we are placing in the random subset
    for i in range(n_subset):
        # select a random element to swap into random subset
        j = randint(i, len(array) - 1)
        array[i], array[j] = array[j], array[i]

    return array[:n_subset]

if __name__ == '__main__':
    print(sample([1, 2, 3, 4, 5], 3))
