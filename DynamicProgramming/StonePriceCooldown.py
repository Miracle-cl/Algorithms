from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        holds = [0] * len(prices)
        solds = holds[:]
        rest = holds[:]
        holds[0] = - prices[0]
        for i in range(1, len(prices)):
            holds[i] = max(holds[i-1], rest[i-1]-prices[i])
            solds[i] = holds[i-1] + prices[i]
            rest[i] = max(solds[i-1], rest[i-1])
        return max(solds[-1], rest[-1])


if __name__ == '__main__':
    ps = [1,2,3,0,2]
    solu = Solution()
    res = solu.maxProfit(ps)
    print(res)