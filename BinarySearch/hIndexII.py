from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        if len(citations) == 1:
            return 1 if citations[0] > 0 else 0
        
        n = len(citations)
        
        def is_hi(h):
            if citations[-h] >= h and citations[n-h-1] <= h:
                return 0 # h is index
            if citations[-h] < h:
                return -1 # h is larger
            return 1 # h is smaller
        
        l, r = 0, min(citations[-1], n)
        while l < r:
            h = (l + r) // 2
            flag = is_hi(h)
            if flag < 0:
                r = h
            elif flag == 0:
                return h
            else:
                l = h + 1
        return l

    def hIndex_1(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n
        while l < r:
            h = (l + r) // 2
            if citations[h] >= n-h:
                r = h
            else:
                l = h + 1
        return n - l

    def hIndex_2(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n
        while l < r:
            h = (l + r) // 2
            if citations[h] > n-h:
                r = h
            elif citations[h] == n-h:
                return n - h
            else:
                l = h + 1
        return n - l


citations = [0,1,3,5,6]
ss = Solution()
res = ss.hIndex(citations)
print(res)