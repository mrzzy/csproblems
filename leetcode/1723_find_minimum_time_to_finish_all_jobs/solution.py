#
# CSProblems
# Leetcode
# 1723. Find Minimum Time to Finish All Jobs
#


class Solution:
    def __init__(self):
        self.min_time = -1

    def minimumTimeRequired(self, jobs: list[int], k: int) -> int:
        self.explore(jobs, 0, [0 for _ in range(k)])
        return self.min_time

    def explore(self, jobs: list[int], j: int, assignments: list[int]):
        complete_time = max(assignments)
        if j >= len(jobs):
            # base case: no more jobs remaining:
            # compute max time taken by all workers
            self.min_time = (
                complete_time
                if self.min_time is None
                else min(self.min_time, complete_time)
            )
            return

        if self.min_time != -1 and complete_time >= self.min_time:
            # skip worse assignment: already or about to be worse then min time
            return

        # try out assignment of jth job to each worker
        explored = set()
        for i in range(len(assignments)):
            # some workers take the same time with current assignments
            # so exploring any one of them would suffice
            if assignments[i] in explored:
                continue

            # suppose we assign the job to this worker
            # recursively explore the assignment of remaining jobs.
            assignments[i] += jobs[j]
            self.explore(jobs, j + 1, assignments)
            assignments[i] -= jobs[j]
            explored.add(assignments[i])
