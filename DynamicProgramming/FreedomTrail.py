# import heapq
from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        c2i = defaultdict(list)
        n = len(ring)
        m = len(key)
        dp = [[0] * n for _ in range(n)]
        for i, char in enumerate(ring):
            c2i[char].append(i)
        for i in range(n):
            for j in range(i+1, n):
                dp[i][j] = min(j - i, n - (j - i))
                dp[j][i] = dp[i][j]

        # if priority_queue then TLE
        cur = [(0, 0)] # steps, char_id, key_id
        # same as viterbi algorithms
        for char in key:
            nxt = []
            for i, v in enumerate(c2i[char]):
                n_step = float('inf')
                for step, u in cur:
                    n_step = min(n_step, step + dp[u][v])
                nxt.append((n_step, v))
            cur = nxt
            #print(cur)
        return min(step for step, _ in cur) + m


# ring = "godding"
# key = "gd"

ring = "caotmcaataijjxi"
key = "oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx"
res = Solution().findRotateSteps(ring, key)
print(res)