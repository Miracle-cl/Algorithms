import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n+1)]
        res = ''
        k -= 1
        while n:
            a = math.factorial(n-1)
            i = k // a
            # print(i, nums, k)
            res += str(nums[i])
            nums = nums[:i] + nums[i+1:]
            k -= i * a
            n -= 1
        return res

    def getPermutation1(self, n: int, k: int) -> str:
        # TLE
        res = [k, '']
        visited = [0] * (n + 1)

        def backtrack(n, string):
            if not res[0]:
                return
            if len(string) == n:
                # print(string)
                res[0] -= 1
                if not res[0]:
                    res[1] = string
                return
            for i in range(1, n+1):
                if visited[i]:
                    continue
                visited[i] = 1
                backtrack(n, string + str(i))
                visited[i] = 0
            return

        backtrack(n, '')
        return res[1]


solu = Solution()
res = solu.getPermutation(9, 331987)
print(res)