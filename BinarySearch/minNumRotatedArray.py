from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        l, r = 0, len(numbers)-1
        while l < r:
            mid = (l + r) // 2
            if numbers[mid] < numbers[r]:
                r = mid
            elif numbers[mid] > numbers[r]:
                l = mid + 1
            else:
                r -= 1
        return numbers[l]


if __name__ == '__main__':
    ss = Solution()
    nums = [1,2,3,4,5,6,]
    for i in range(len(nums)):
        nn = nums[i:] + nums[:i]
        print(nn, ss.minArray(nn))