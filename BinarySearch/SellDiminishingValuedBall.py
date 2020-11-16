from typing import List


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        mode = 10 ** 9 + 7
        l, r = 0, max(inventory)
        while l < r:
            T = (l + r) // 2
            xx = sum(ai - T for ai in inventory if ai >= T)
            if xx > orders:
                l = T + 1
            else:
                r = T
        ans = 0
        # print(l)
        for ai in inventory:
            if ai >= l:
                # l+1, ... ai
                ans += (l+1 + ai) * (ai - l) // 2
                orders -= ai - l
        # print(orders, ans)
        ans += orders * l
        return ans % mode



# inventory = [2,8,4,10,6]
# orders = 20

# inventory = [2,5]
# orders = 4

# inventory = [3,5]
# orders = 6

inventory = [1000000000]
orders = 1000000000

ans = Solution().maxProfit(inventory, orders)
print(ans)