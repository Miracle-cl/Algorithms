class Solution:
    def jump(self, nums):
        step = 0
        cur = 0
        i = 0
        size = len(nums)
        while cur < size - 1:
            step += 1
            prev = cur
            while i <= prev:
                cur = max(cur, i + nums[i])
                i += 1
            if prev == cur:
                return -1 # cannot reach
        return step


# nums = [1,1,5,1,1,1]
nums = [3,2,1,1,4]
# nums = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
s = Solution()
print(s.jump(nums))
