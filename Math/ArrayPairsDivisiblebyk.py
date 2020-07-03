from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = [0] * k
        for x in arr:
            xk = (x % k + k) % k # x < 0
            freq[xk] += 1

        for i in range(1, k):
            if freq[i] != freq[k - i]:
                return False

        if k % 2 == 0 and freq[k//2] % 2 != 0:
            # i == k - i
            return False

        return freq[0] % 2 == 0 # i == 0


# [1,2,3,4,5,10,6,7,8,9]
# 5, T
# [1,2,3,4,5,6]
# 7, T
# [1,2,3,4,5,6]
# 10, F
# [-10,10]
# 2, T
# [-1,1,-2,2,-3,3,-4,4]
# 3, T