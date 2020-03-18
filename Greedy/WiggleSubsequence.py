from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 2:
            return size
        prev, ptag, length = nums[0], None, 1
        for i in range(1, size):
            if nums[i] > prev:
                prev = nums[i]
                if ptag == '-' or ptag is None:
                    ptag = '+'
                    length += 1
            elif nums[i] < prev:
                prev = nums[i]
                if ptag == '+' or ptag is None:
                    ptag = '-'
                    length += 1
        return length


if __name__ == '__main__':
    solu = Solution()
    # nums = [1,17,5,10,13,15,10,5,16,8]
    # nums = [1,2,3,4,5]
    nums = [1,7,4,9,2,5]
    res = solu.wiggleMaxLength(nums)
    print(res)
