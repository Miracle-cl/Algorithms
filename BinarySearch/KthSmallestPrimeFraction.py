from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        n = len(A)
        l, r = 0, 1
        _mem = {}

        def f(i, j):
            if (i, j) not in _mem:
                _mem[(i, j)] = A[i] / A[j]
            return _mem[(i, j)]

        def count(target):
            cnt = 0
            val = 0
            x, y = None, None
            j = 1
            for i in range(n-1):
                while j < n and f(i, j) > target:
                    j += 1
                if j == n:
                    break
                cnt += n - j
                if val < f(i, j):
                    val, x, y = f(i, j), A[i], A[j]
            return cnt, x, y

        while l < r:
            mid = (l + r) / 2
            cnt, x, y = count(mid)
            if cnt < K:
                l = mid
            elif cnt > K:
                r = mid
            else:
                return [x, y]
        return []


# A = [1, 2, 3, 5], K = 3