from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def count(tgt):
            cnt = 1
            loc = position[0]
            for p in position:
                if p - loc >= tgt:
                    cnt += 1
                    loc = p
                if cnt >= m:
                    break
            return cnt
                
        position.sort()
        left = 0
        right = position[-1] - position[0] + 1
        while left < right:
            mid = (left + right) // 2
            cnt = count(mid)
            # print(mid, cnt)
            if cnt >= m:
                left = mid + 1
            else:
                right = mid
        ### in competition, always wrong is as return left
        return left - 1 # first left value of left boundary is satisfied


ss = Solution()
# position= [975017321,74045490,415097519,76628781,843696647,709774845,493571894,23388841,184522636,794748308,
#            746534625,248911596,490131472,321479956,335523769,748628710,226578862,959858170,810159464,85795199,
#            898777852,163699246,289742726,945822015]
# m = 4
# position = [85,24,66,57,71,43,62,93,35,23,41,8,92,96,63,77,75,26,79,78]
# m = 17
# position = [94,95,37,30,67,7,5,44,26,55,42,28,97,19,100,74,13,88,18]
# m = 7
position = [5999,2816,4264,2051,1731,5565]
m = 2
res = ss.maxDistance(position, m)
print(res)