from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nn = [1] + nums + [1]
        size = len(nn)
        dp = [[0] * size for _ in range(size)]
        # length == 1:
        for i in range(1, size-1):
            dp[i][i] = nn[i-1] * nn[i] * nn[i+1]
        for length in range(2, size-1):
            for s in range(1, size-1):
                e = s + length - 1
                if e > size-2:
                    continue
                for k in range(s, e+1):
                    tmp = dp[s][k-1] + nn[s-1]*nn[k]*nn[e+1] + dp[k+1][e]
                    dp[s][e] = max(tmp, dp[s][e])
        # for i in range(len(dp)):
        #     print(dp[i])
        return dp[1][size-2]


if __name__ == '__main__':
    solu = Solution()
    nums = [3,1,5,8]
    res = solu.maxCoins(nums)
    print(res)