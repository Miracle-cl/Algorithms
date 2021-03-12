class Solution:
    def add(self, a: int, b: int) -> int:
        mask = 0xffffffff
        a &= mask
        b &= mask
        while b:
            a, b = a ^ b, ((a & b) << 1) & mask
        # 0x7fffffff == (1 << 31) - 1
        return ~(a ^ mask) if a > 0x7fffffff else a


res = Solution().add(-1, -2)
print(res)