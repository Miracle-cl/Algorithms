from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # O(nlog(sum(nums))): faster
        def count_groups(target):
            k = 0
            groups = 0
            for n in nums:
                groups += n
                if groups == target:
                    groups = 0
                    k += 1
                elif groups > target:
                    groups = n
                    k += 1
            if groups > 0:
                k += 1
            return k

        l, r = max(nums), sum(nums)+1
        while l < r:
            mid = (l + r) // 2
            k = count_groups(mid)
            # print(mid, k)
            if k <= m:
                r = mid
            else:
                l = mid + 1

        return l

    def splitArray_dp(self, nums: List[int], m: int) -> int:
        # dp: O(mn^2): slower
        # dp[n][m] = min(max(dp[k][m-1], sum(k+1,n)) for k in range(m-1, n))
        n = len(nums)
        _f = {}
        prefix_s = [0] + nums
        for i in range(n):
            prefix_s[i+1] += prefix_s[i]

        def f(n, m):
            if (n, m) in _f:
                return _f[(n,m)]
            if m == 1:
                return prefix_s[n]-prefix_s[0]     
            
            _f[(n,m)] = float('inf')
            for i in range(m-1, n):
                ki = max(f(i, m-1), prefix_s[n]-prefix_s[i])
                _f[(n,m)] = min(_f[(n,m)], ki)
            return _f[(n,m)]

        return f(n, m)


# Input:
# nums = [7,2,5,10,8]
# m = 2

# Output:
# 18