from typing import List
from collections import defaultdict


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        # (a - b) % k == 0  <-> a%k == b%k
        tol = ans = 0
        record = defaultdict(int)
        record[0] = 1
        for a in A:
            tol += a
            r = tol % K
            record[r] += 1
        
        for r, c in record.items():
            # from c choose 2
            ans += c * (c -1) // 2
        return ans

    def subarraysDivByK_1(self, A: List[int], K: int) -> int:
        # (a - b) % k == 0  <-> a%k == b%k
        tol = ans = 0
        record = defaultdict(int)
        record[0] = 1
        for a in A:
            tol += a
            r = tol % K
            ans += record[r]
            record[r] += 1
        
        # for r, c in record.items():
        #     ans += c * (c -1) // 2
        return ans


A = [4,5,0,-2,-3,1]
K = 5