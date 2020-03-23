class Solution:
    def getMoneyAmount(self, n: int) -> int:
        _mem = {}

        def helper(l, r):
            if l >= r:
                return 0
            if l + 1 == r:
                return l
            if (l, r) in _mem:
                return _mem[(l, r)]
            val = float('inf')
            for k in range(l, r):
                tmp = max(helper(l, k-1), helper(k+1, r)) + k
                val = min(val, tmp)
            _mem[(l, r)] = val
            return val

        return helper(1, n)

    def getMoneyAmount_dp(self, n: int) -> int: # faster
        ## Minimax Algorithms
        dp = [[0] * (1+n) for _ in range(1+n)]
        for length in range(2, 1+n):
            for s in range(1, n+2-length):
                e = s+length-1
                # if e > n :
                #     continue
                dp[s][e] = float('inf')
                for k in range(s, e):
                    tmp = k + max(dp[s][k-1], dp[k+1][e])
                    # dp[s][e] = min(tmp, dp[s][e]) if dp[s][e] > 0 else tmp
                    dp[s][e] = min(tmp, dp[s][e]) # faster then if
        # for i in range(1, 1+n):
        #     print(i, dp[1][i])
        return dp[1][n]


if __name__ == '__main__':
    solu = Solution()
    n = 21
    res = solu.getMoneyAmount_dp(n)
    # for i in range(n):
    #     res = solu.getMoneyAmount(i)
    #     print(i, res)