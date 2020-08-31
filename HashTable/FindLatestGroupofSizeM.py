from typing import List


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        lens = [0] * (n+2)
        cnts = [0] * (n+2)

        ans = -1
        for i in range(n):
            x = arr[i]
            left = lens[x-1]
            right = lens[x+1]
            length = left + right + 1
            # update boundary
            lens[x - left] = lens[x + right] = length
            cnts[left] -= 1
            cnts[right] -= 1
            cnts[length] += 1
            # print(lens)
            if cnts[m]:
                ans = i + 1
                
        return ans



arr = [3,5,1,2,4]
m = 1
ss = Solution()
res = ss.findLatestStep(arr, m)
print(res)