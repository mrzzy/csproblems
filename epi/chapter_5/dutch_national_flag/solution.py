#
# CSProblems
# Elements of Programming Interviews
# 5.1 Dutch National Flag Problem
#

def partition(array: list[int], pivot: int) -> list[int]:
    """Partitions given array into 3 partitions (<, =, >) to element at given pivot index."""
    # defines the start and end of the less than (lt), greater than (gt) partitions
    lt, i, gt = -1, 0, len(array)
    value = array[pivot]
    
    while i < gt:
        if array[i] < value:
            # swap into left lt partition
            lt += 1
            array[lt], array[i] = array[i], array[lt]
        if array[i] > value:
            # swap into right gt partition
            gt -= 1
            array[gt], array[i] = array[i], array[gt]

        i += 1
    return array

if __name__ == '__main__':
    print(partition([3,2,4,1,3,4,3,3,1,3,2], 0))
