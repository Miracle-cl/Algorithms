import math

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        limit = math.pow(10, n)
        used = [0] * 10

        def backtrack(cur, used):
            if cur >= limit:
                return 0
            begin = 1 if cur == 0 else 0
            total = 1
            for i in range(begin, 10):
                if used[i]:
                    continue
                used[i] = 1
                total += backtrack(cur*10+i, used)
                used[i] = 0
            return total
            
        #used[0] = 1
        num = backtrack(0, used)
        return num

    
if __name__ == '__main__':
    solu = Solution()
    n = 3
    res = solu.countNumbersWithUniqueDigits(n)
    print(res)