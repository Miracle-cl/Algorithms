from typing import List


class Solution:
    def minimumTimeRequired_0(self, jobs: List[int], k: int) -> int:
        # State Pressure DP

        # tot[i] : time costs to finish all jobs of state i 
        n_jobs = len(jobs)
        states = 1 << n_jobs
        tot = [0] * states
        for i in range(1, states):
            for j in range(n_jobs):
                if (i >> j) & 1 == 0:
                    continue
                tot[i] = tot[i - (1 << j)] + jobs[j]
                break
        # print(tot)

        # dp[j][i] : time cost of [first j workers & state i jobs]
        # dp[j][i] = min( max(dp[j-1][i-s], tot[s]) for s in (subset of i) )
        dp = [[tot[-1]] * states for _ in range(k)]
        for i in range(states):
            dp[0][i] = tot[i]
            
        for j in range(1, k):
            for i in range(states):
                s = i
                while s > 0:
                    dp[j][i] = min(dp[j][i], max(dp[j-1][i-s], tot[s]))
                    s = (s-1) & i
        return dp[k-1][states-1]

    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        # State Pressure DP - binary search

        # if work_time is known, then need dp[i] workers in state i at least
        # As work_time up, dp[i] down (worker num down)
        # dp[i] = min(dp[i-s] + 1 for s in subset of i if tot[s] <= wt)

        n = len(jobs)
        states = 1<<n
        tot = [0] * states
        for i in range(1, states):
            for j in range(n):
                if (i >> j) & 1 == 0:
                    continue
                tot[i] = tot[i - (1 << j)] + jobs[j]
                break
                
        l = min(jobs)
        r = tot[states-1] + 1
        while l < r:
            limit_t = (l + r) // 2
            # get dp[states-1]
            dp = [k+1] * states
            dp[0] = 0
            for i in range(1, states):
                s = i
                while s > 0:
                    if tot[s] <= limit_t:
                        dp[i] = min(dp[i], dp[i-s] + 1)
                    s = (s-1) & i
            
            if dp[states-1] > k:
                l = limit_t + 1
            else:
                r = limit_t

        return l


# jobs = [1,2,4,7,8]
# k = 2