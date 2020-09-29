from typing import List


class Solution:
    def busRapidTransit(self, target: int, inc: int, dec: int, jump: List[int], cost: List[int]) -> int:
        # from target to 0 is OK
        # from 0 to target too slow TLE
        n = len(jump)
        mode = 1000000007
        mem = {}

        def search(tgt):
            if tgt == 0:
                return 0
            if tgt == 1:
                return inc
            if tgt in mem:
                return mem[tgt]
            ans = inc * tgt
            for i in range(n):
                former, residual = tgt // jump[i], tgt % jump[i]
                if residual == 0:
                    ans = min(ans, search(former) + cost[i])
                else:
                    # jump + forward
                    less = search(former) + cost[i] + inc * residual
                    # jump + backward
                    more = search(former+1) + cost[i] + dec * (jump[i]-residual)
                    ans = min(ans, less, more)
            mem[tgt] = ans
            return mem[tgt]

        return search(target) % mode


# LCP 20. 快速公交
target = 612
inc = 4
dec = 5
jump = [3,6,8,11,5,10,4]
cost = [4,7,6,3,7,6,4]

# 983423205
# 448232
# 963363
# [38856,505823,835262,569086,958567,630647,350011,311421,898695,57358]
# [460603,941593,107678,409305,899055,915790,299351,563865,516575,747521]

ss = Solution()
res = ss.busRapidTransit(target, inc, dec, jump, cost)
print(res)