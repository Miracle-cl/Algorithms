from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters)
        while l < r:
            mid = (l + r) // 2
            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return letters[r] if r < len(letters) else letters[0]


let = ['c', 'f', 'j']
tar = 'c'
ss = Solution()
print(ss.nextGreatestLetter(let, tar))
