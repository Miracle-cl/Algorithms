class Solution:
    def divide(self, dividend, divisor):
        m = abs(dividend)
        n = abs(divisor)
        res = 0
        if m < n:
            return 0
        while m >= n:
            t, p = n, 1
            while (m > (t << 1)):
                t <<= 1
                p <<= 1
            res += p
            m -= t
        res = -res if (dividend < 0) ^ (divisor < 0) else res
        return res


test_cases = [[-10, 3], [10, 3], [-2147483648, -1]]

solu = Solution()
for i in range(3):
    print(solu.divide(test_cases[i][0], test_cases[i][1]))
# print(3 << 1)
