from typing import List


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # 4984 ms
        _mem = {}
        def f(i, j):
            if (i, j) not in _mem:
                _mem[(i, j)] = (i+1) * (j+1)
            return _mem[(i, j)]
            
        l, r = f(0, 0), f(m-1, n-1)

        def count(target):
            cnt = 0
            i, j = m-1, 0
            while i >= 0 and j < n:
                if f(i, j) <= target:
                    j += 1
                else:
                    cnt += j
                    i -= 1
            if i >= 0:
                cnt += (i+1) * j
            return cnt

        while l < r:
            mid = (l + r) // 2
            if count(mid) < k:
                l = mid + 1
            else:
                r = mid
        return l

    def findKthNumber_1(self, m: int, n: int, k: int) -> int:
        # 924ms
        def count(target):
            cnt = sum(min(n, target//ri) for ri in range(1, 1+m))
            return cnt

        l, r = 1, m * n + 1
        while l < r:
            mid = (l + r) // 2
            if count(mid) < k:
                l = mid + 1
            else:
                r = mid
        return l

    def findKthNumber_2(self, m: int, n: int, k: int) -> int:
        # 1160ms
        def count(target):
            # pruning
            cnt = 0
            for ri in range(1, 1+m):
                c = min(n, target//ri)
                cnt += c
                if c == 0 or cnt >= k:
                    break
            return cnt

        l, r = 1, m * n + 1
        while l < r:
            mid = (l + r) // 2
            if count(mid) < k:
                l = mid + 1
            else:
                r = mid
        return l