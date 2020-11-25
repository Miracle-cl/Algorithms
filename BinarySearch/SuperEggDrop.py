# dp[0, n] = 0
# dp[1, n] = n
# dp[k, n] = min(1 + max(dp[k-1, i], dp[k, n-i]) for i in range(1, n))
# at i drop: if broken then dp[k-1, i-1], else dp[k, n-i]
# dp[k-1, i-1] is a increasing func
# dp[k, n-i] is a decreasing func


class Solution:
    def superEggDrop_TLE(self, K: int, N: int) -> int:
        mem = {}
        def f(k, n):
            if k == 0:
                return 0
            if k == 1:
                return n
            if n <= 1:
                return n
            if (k, n) in mem:
                return mem[k, n]
            ans = float('inf')
            for i in range(1, n):
                ans = min(ans, 1 + max(f(k-1, i-1), f(k, n-i)))
            mem[k, n] = ans
            return ans
        return f(K, N)


    def superEggDrop(self, K: int, N: int) -> int:
        mem = {}
        def f(k, n):
            if k == 0:
                return 0
            if k == 1:
                return n
            if n <= 1:
                return n
            if (k, n) in mem:
                return mem[k, n]

            l, r = 1, n
            while l < r:
                i = (l + r) // 2
                broken = f(k-1, i-1)
                unbroken = f(k, n-i)
                if broken < unbroken:
                    l = i + 1
                else:
                    r = i
            # mem[k, n] = 1 + max(f(k-1, l-1), f(k, n-l))
            # print(f(k-1, l-1), f(k, n-l))
            mem[k, n] = 1 + f(k-1, l-1)
            return mem[k, n]

        return f(K, N)


if __name__ == '__main__':
    res = Solution().superEggDrop(2, 100)
    print(res)