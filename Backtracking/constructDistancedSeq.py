from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        lens = 2 * n - 1
        resutls = [0] * lens
        used = [0] * (1+n)

        def backtrack(i):
            # print(i, resutls)
            if i == lens:
                return True
            if resutls[i] > 0:
                return backtrack(i+1)
            for k in range(n, 0, -1):
                if used[k]:
                    continue
                if k > 1 and (i+k >= lens or resutls[i+k] > 0):
                    continue
                resutls[i] = k
                if k > 1:
                    resutls[i+k] = k
                used[k] = 1
                if not backtrack(i+1):
                    resutls[i] = 0
                    if k > 1:
                        resutls[i+k] = 0
                    used[k] = 0
            return resutls[i] > 0

        backtrack(0)
        return resutls


if __name__ == '__main__':
    res = Solution().constructDistancedSequence(10)
    print(res)