class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        l1 = l2 = 0
        n1, n2 = len(nums1), len(nums2)
        k = (n1 + n2 + 1) // 2
        if n1 < n2:
            return self.findK(nums1, nums2, k)
        else:
            return self.findK(nums2, nums1, k)

    def findK(self, nums1, nums2, k):
        l, r = 0, len(nums1)
        while l < r:
            m1 = (l + r) // 2
            m2 = k - m1
            if m2 < 0:
                r = m1
            else:
                if nums1[m1] < nums2[m2-1]:
                    l = m1 + 1;
                else:
                    r = m1
        m1, m2 = l, k - l
        if m1 <= 0:
            ck_1 = nums2[m2-1]
        elif m2 <= 0:
            ck_1 = nums1[m1-1]
        else:
            ck_1 = max(nums1[m1-1], nums2[m2-1])

        # neg_inf, pos_inf = float('-inf'), float('inf')
        # ck_1 = max(nums1[m1-1]if m1 > 0 else neg_inf, nums2[m2-1] if m2 > 0 else neg_inf)

        if (len(nums1) + len(nums2)) % 2 == 1:
            return ck_1
        else:
            if m1 >= len(nums1):
                ck = nums2[m2]
            elif m2 >= len(nums2):
                ck = nums1[m1]
            else:
                ck = min(nums1[m1], nums2[m2])
            # ck = min(nums1[m1] if m1 < len(nums1) else pos_inf, nums2[m2] if m2 < len(nums2) else pos_inf)
            return (ck_1 + ck) / 2



s = Solution()
nums1 = [1,2]
nums2 = [3,4]
res = s.findMedianSortedArrays(nums1, nums2)
print(res)
