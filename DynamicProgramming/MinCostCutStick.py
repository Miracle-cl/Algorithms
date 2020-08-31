from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        m = len(cuts)
        cuts.sort()
        _f = dict()
        
        def f(i, j, l, r):
            # min cost to from i-th cut to j-th cut in range (l, r)
            # l = cut[i-1], r = cuts[j+1]
            if i > j:
                return 0
            if i == j:
                return r - l # one cut, len(stick)
            if (i, j) in _f:
                return _f[i, j]
            ans = float('inf')
            for k in range(i, j+1):
                ans = min(ans, f(i, k-1, l, cuts[k]) + f(k+1, j, cuts[k], r))
            _f[i, j] =  ans + r - l
            return _f[i, j]
        return f(0, m-1, 0, n)


ss= Solution()
n = 9
cuts = [1,2,4,5,6]
res = ss.minCost(n, cuts)
print(res)