from typing import List


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        def choose_max_s(strs: List[str]):
            if len(strs) < 2:
                return str
            res = strs[0]
            for i in range(1, len(strs)):
                tmp = sorted([c for c in strs[i]], reverse=True)
                tmp = ''.join(tmp)
                if len(tmp) > len(res):
                    res = tmp
                elif len(tmp) == len(res) and tmp > res:
                    res = tmp
            return [res]

        c2i = {}
        minv = float('inf')
        for i, c in enumerate(cost, 1):
            c2i[c] = str(i)
            minv = min(minv, c)

        # dp[T] = dp[T-c] + c2i[c]
        dp = [[] for _ in range(1+target)]
        for c, s in c2i.items():
            if c > target:
                continue
            dp[c].append(s)
        
        for t in range(1+minv, 1+target):
            for c, s in c2i.items():
                if t > c and dp[t-c]:
                    dp[t].extend([x + s for x in dp[t-c]])
            if len(dp[t]) > 1:
                dp[t] = choose_max_s(dp[t])

        return dp[target][0]


cost = [4,3,2,5,6,7,2,5,5]
target = 9

ss = Solution()
res = ss.largestNumber(cost, target)
print(res)