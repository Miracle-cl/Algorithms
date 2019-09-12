class Solution(object):
    def findNumberOfLIS(self, nums):
        N = len(nums)
        if N < 2:
            return N
        lengths = [0] * N #lengths[i] = longest ending in nums[i]
        counts = [1] * N #count[i] = number of longest ending in nums[i]

        for j in range(N):
            for i in range(j):
                if nums[i] < nums[j]:
                    if lengths[i] >= lengths[j]:
                        lengths[j] = 1 + lengths[i]
                        counts[j] = counts[i]
                    elif lengths[i] + 1 == lengths[j]:
                        print(i, j, lengths, counts)
                        counts[j] += counts[i]
                        print(i, j, lengths, counts)

            print(j, lengths, counts)

        longest = max(lengths)
        print(lengths, counts)
        return sum(c for i, c in enumerate(counts) if lengths[i] == longest)


solu = Solution()
nums = [1,3,5,4,7,7]
res = solu.findNumberOfLIS(nums)
print(res)
