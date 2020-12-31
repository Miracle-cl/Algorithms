from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        has_stock = -prices[0]
        no_stock = 0
        n = len(prices)
        for i in range(1, n):
            has_stock, no_stock = max(no_stock - prices[i], has_stock), max(prices[i] + has_stock - fee, no_stock)

        return no_stock

    def maxProfit_0(self, prices: List[int], fee: int) -> int:
        has_stock = [-prices[0]]
        no_stock = [0]
        n = len(prices)
        for i in range(1, n):
            has_stock.append(max(no_stock[-1] - prices[i], has_stock[-1]))
            no_stock.append(max(prices[i] + has_stock[-1] - fee, no_stock[-1]))

        return no_stock[-1]


prices = [1, 3, 2, 8, 5, 11, 4, 9]
fee = 2
res = Solution().maxProfit(prices, fee)
print(res)