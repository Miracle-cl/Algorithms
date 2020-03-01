class Solution:
    def integerBreak(self, n: int) -> int:
        _mem = {}

        def recursive(n):
            if n == 1 or n == 2:
                return 1
            if n in _mem:
                return _mem[n]
            mv = 0
            for i in range(1, 1+n//2):
                ll = max(i, recursive(i))
                rr = max(n-i, recursive(n-i))
                mv = max(mv, ll*rr)
            _mem[n] = mv
            return mv

        max_value = recursive(n)
        return max_value


if __name__ == '__main__':
    solu = Solution()
    n = 2
    res = solu.integerBreak(n)
    print(res)