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

    def maxCoins_2(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        size = len(nums)
        dp = [[0] * size for _ in range(size)]
        for i in range(1, size-1):
            dp[i][i] = nums[i-1] * nums[i] * nums[i+1]
            
        for length in range(2, size-1):
            for begin in range(1, size-length):
                end = begin + length - 1
                prod_ = nums[begin-1] * nums[end+1]
                for last in range(begin, end+1):
                    # last balloon burst
                    tmp = dp[begin][last-1] + prod_ * nums[last] + dp[last+1][end]
                    dp[begin][end] = max(tmp, dp[begin][end])

        return dp[1][size-2]


    def maxCoins_3(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        # print(n, nums)
        _dp = {}
        def dp(i, j):
            # put Balloon in (i, j), i, j is not include
            # same as: k-th balloon is last burst
            if i + 1 >= j:
                return 0
            if (i, j) in _dp:
                return _dp[i, j]
            ans = 0
            for k in range(i+1, j):
                ans = max(ans, nums[i]*nums[k]*nums[j] + dp(i, k) + dp(k, j))
            _dp[i, j] = ans
            return ans
                
        return dp(0, n -1)


if __name__ == '__main__':
    solu = Solution()
    nums = [3,1,5,8]
    res = solu.maxCoins(nums)
    print(res)