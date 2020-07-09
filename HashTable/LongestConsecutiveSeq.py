from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # hash tabel
        n_set = set(nums)
        lens = 0

        for n in nums:
            if n-1 in n_set:
                continue
            cur = n
            cur += 1
            while cur in n_set:
                cur += 1
            lens = max(lens, cur - n)
        return lens

    def longestConsecutive_disjointset(self, nums: List[int]) -> int:
        # disjoint set
        lens = 0
        parent = {}

        def find(x):
            if parent[x] in parent:
                parent[x] = find(parent[x])
            return parent[x]

        for n in nums:
            parent[n] = n - 1
            
        for n in nums:
            root = find(n)
            # print(parent)
            lens = max(lens, n - root)
        return lens


# [100, 4, 200, 1, 3, 2] -> 4