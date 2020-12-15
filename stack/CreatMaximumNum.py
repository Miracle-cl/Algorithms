from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def max_sub(nums, n, k):
            stk = []
            for i, num in enumerate(nums):
                while stk and num > stk[-1] and n-i > k-len(stk):
                    stk.pop()
                if len(stk) < k:
                    stk.append(num)
            return stk

        def merge(sub1, sub2):
            ans = []
            m, n = len(sub1), len(sub2)
            i = j = 0
            while i < m and j < n:
                if sub1[i] < sub2[j]:
                    ans.append(sub2[j])
                    j += 1
                elif sub1[i] > sub2[j]:
                    ans.append(sub1[i])
                    i += 1
                else: # sub1[i] == sub2[j]
                    ii, jj = i+1, j+1
                    while ii < m and jj < n and sub1[ii] == sub2[jj]:
                        ii += 1
                        jj += 1
                    if ii >= m or (jj < n and sub1[ii] < sub2[jj]):
                        ans.append(sub2[j])
                        j += 1
                    else:
                        ans.append(sub1[i])
                        i += 1
            while i < m:
                ans.append(sub1[i])
                i += 1
            while j < n:
                ans.append(sub2[j])
                j += 1
            return ans

        m, n = len(nums1), len(nums2)
        ans = (nums1 + nums2)[:k]
        for i in range(1+k):
            j = k - i
            if i > m or j > n:
                continue
            sub1 = max_sub(nums1, m, i)
            sub2 = max_sub(nums2, n, j)
            x = merge(sub1, sub2)
            # print(x)
            if ans < x:
                ans = x
        return ans


# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5


nums1 = [2,5,6,4,4,0]
nums2 = [7,3,8,0,6,5,7,6,2]
k = 15
res = Solution().maxNumber(nums1, nums2, k)
print(res)