#
# CSProblems
# Neetcode
# NC5. Top K Frequent Elements
#

from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count elements
        counts = Counter(nums)
        # regroup elements by count
        max_count = max(counts.values())
        count_grps = [[] for _ in range(max_count + 1)]
        for i, count in counts.items():
            count_grps[count].append(i)

        # collect top k frequent by iterating count groups backward
        top_k = []
        while k > 0:
            while len(count_grps) > 0 and len(count_grps[-1]) > 0:
                top_k.append(count_grps[-1].pop())
                k -= 1
                if k == 0:
                    return top_k
            count_grps.pop()
        raise ValueError("Top k larger then given no. of elements")
