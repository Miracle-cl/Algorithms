from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sv = sum(nums)
        if (not nums) or sv % k != 0:
            return False
        if k == 1:
            return True
        tag = sv // k
        nums.sort()

        if nums[-1] > tag:
            return False

        visited = [0] * len(nums)
        while nums and nums[-1] == tag:
            nums.pop()
            k -= 1

        # def backtrack(start, cur_sum, tag, k):
        #     if k == 1:
        #         return True
        #     if cur_sum == tag:
        #         return backtrack(0, 0, tag, k-1)
        #     if cur_sum > tag:
        #         return False
        #     for i in range(start, len(nums)):
        #         if visited[i]:
        #             continue
        #         visited[i] = 1
        #         if backtrack(i+1, cur_sum+nums[i], tag, k):
        #             return True
        #         visited[i] = 0
        #     return False
        def backtrack(start, cur_sum, tag, k): # pruning
            if k == 1:
                return True
            if cur_sum == tag:
                return backtrack(0, 0, tag, k-1)

            for i in range(start, len(nums)):
                if visited[i]:
                    continue
                if cur_sum+nums[i] > tag:
                    break
                visited[i] = 1
                if backtrack(i+1, cur_sum+nums[i], tag, k):
                    return True
                visited[i] = 0
            return False

        return backtrack(0, 0, tag, k)


if __name__ == '__main__':
    solu = Solution()
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    # nums = [10,10,10,7,7,7,7,7,7,6,6,6]
    # k = 3

    res = solu.canPartitionKSubsets(nums, k)
    print(res)

