from typing import List

class Solution:
    def countBits(self, num: int) -> List[int]:
        # i & (i-1) : check if % 2 == 0
        nums = [0] * (num + 1)
        nums[0] = 0
        for i in range(1, num+1):
            nums[i] = nums[i & (i-1)] + 1
        return nums


if __name__ == '__main__':
    solu = Solution()
    res = solu.countBits(16)
    print(res)