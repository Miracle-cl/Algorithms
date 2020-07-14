from typing import List


class FenwickTree:
    def __init__(self, n):
        self._sums = [0 for _ in range(n + 1)]
        
    def update(self, i, delta):
        while i < len(self._sums):
            self._sums[i] += delta
            i += self.low_bit(i)
    
    def query(self, i):
        s = 0
        while i > 0:
            s += self._sums[i]
            i -= self.low_bit(i)
        return s
    
    @staticmethod
    def low_bit(x):
        return x & -x


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.ft = FenwickTree(len(nums))
        for i, n in enumerate(nums, 1):
            self.ft.update(i, n)

    def update(self, i: int, val: int) -> None:
        self.ft.update(i+1, val-self.nums[i])
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        return self.ft.query(j+1) - self.ft.query(i)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

if __name__ == '__main__':
    nums = [1, 3, 5]
    na9 = NumArray(nums)
    r1 = na9.sumRange(0, 2)
    na9.update(1, 2)
    r2 = na9.sumRange(0, 2)
    print(r1, r2)

    # test2
    nums = [2, 1, 5, 3, 4]
    na15 = NumArray(nums)
    r1 = na15.sumRange(3, 4)
    r2 = na15.sumRange(2, 2)
    # na15.update(2, 0)
    r3 = na15.sumRange(1, 3)
    print(r1, r2, r3)