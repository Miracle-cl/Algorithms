from typing import List


class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        prefix = [0]
        for a in A:
            prefix.append(prefix[-1] + a)
            
        # sums(A[l : r]) = prefix[r] - prefix[l]

        _f = {}
        def f(r, k):
            # max score of {a[0], a[1], .. a[r-1]} - k group 
            if r == k:
                return prefix[r] # sum(A[0:r])
            if k == 1:
                return prefix[r] / r # sum(A[:r]) / r
            if (r, k) in _f:
                return _f[r, k]
            ans = 0
            for i in range(k-1, r):
                ans = max(ans,  f(i, k-1) + sum(A[i:r]) / (r-i))
            _f[r, k] = ans
            return ans

        return f(len(A), K)