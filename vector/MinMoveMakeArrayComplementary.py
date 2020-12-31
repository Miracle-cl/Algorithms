from typing import List


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        delta = [0] * (2 * limit + 2)
        for i in range(n//2):
            if nums[i] <= nums[n-i-1]:
                a, b = nums[i], nums[n-i-1]
            else:
                a, b = nums[n-i-1], nums[i]
            delta[2] += 2
            delta[a+1] -= 1
            delta[a+b] -= 1
            delta[a+b+1] += 1
            delta[b+limit+1] += 1
            
        presum = 0
        ans = delta[2]
        for i in range(2, 2 * limit + 1):
            presum += delta[i]
            ans = min(ans, presum)
        return ans

    def minMoves_TLE(self, nums: List[int], limit: int) -> int:
        # TLE
        n = len(nums)
        ab = []
        for i in range((n+1)//2):
            if nums[i] <= nums[n-i-1]:
                ab.append((nums[i], nums[n-i-1]))
            else:
                ab.append((nums[n-i-1], nums[i]))
                
        ans = n
        for t in range(2, 2*limit + 1):
            tmp = 0
            for a, b in ab:
                if t == a + b:
                    continue
                if a + 1 <= t < b + limit + 1:
                    tmp += 1
                else:
                    tmp += 2
            ans = min(ans, tmp)
            
        return ans


# nums = [1,2,2,1]
# limit = 2

nums = [3,1,2,1,2,3,3,1,2,3,2,2,1,2,3,3,3,1,1,2,3,2,1,1,2,3,3,3,1,3,3,1,1,2,2,2,2,2,1,3,1,2,2,2]
limit = 3

res = Solution().minMoves(nums, limit)
print(res)