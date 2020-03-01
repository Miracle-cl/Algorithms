from typing import List

class Solution:
    def __init__(self):
        self._mem = {}

    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        if tuple(needs) in self._mem:
            return self._mem[tuple(needs)]

        if all(n == 0 for n in needs):
            return 0

        min_val = self.dot(price, needs)
        for item in special:
            if any(a < b for a, b in zip(needs, item[:-1])):
                continue
            new_needs = [a - b for a, b in zip(needs, item[:-1])]
            val = self.shoppingOffers(price, special, new_needs) + item[-1]
            min_val = min(min_val, val)

        self._mem[tuple(needs)] = min_val
        return min_val
        
    def dot(self, price, needs):
        return sum(a * b for a, b in zip(price, needs))


if __name__ == '__main__':
    solu = Solution()
    price, special, needs = [2,5], [[3,0,5],[1,2,10]], [3,2]
    res = solu.shoppingOffers(price, special, needs)
    print(res)


# [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]