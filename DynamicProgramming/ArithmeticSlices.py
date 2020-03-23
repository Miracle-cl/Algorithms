from typing import List

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        # DP func
        if len(A) < 3:
            return 0

        dp = [0] * len(A)
        sums = 0
        for i in range(2, len(A)):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                dp[i] = dp[i-1] + 1
                sums += dp[i]
        return sums

    def numberOfArithmeticSlices1(self, A: List[int]) -> int:
        # math func
        if len(A) < 3:
            return 0

        start, delt = 0, A[1]-A[0]
        res = 0
        for i in range(2, len(A)):
            tmp = A[i]-A[i-1]
            if tmp != delt:
                length = i - start
                if length > 2:
                    # print(length)
                    res += (length-1) * (length-2) // 2
                start = i-1
                delt = tmp
        length = i - start + 1
        if length > 2:
            # print(length)
            res += (length-1) * (length-2) // 2
        return res


if __name__ == '__main__':
    solu = Solution()
    A = [1,2,3,4,5]
    res = solu.numberOfArithmeticSlices(A)
    print(res)