class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a >= 0 and b >= 0:
            return self.adder(a, b)
        if a <= 0 and b <= 0:
            return -self.adder(-a, -b)
        if a > 0 and b < 0:
            if a > -b:
                return self.subtractor(a, -b)
            elif a < -b:
                return -self.subtractor(-b, a)
            else:
                return 0
        if a < 0 and b > 0:
            if -a > b:
                return -self.subtractor(-a, b)
            if -a < b:
                return self.subtractor(b, -a)
            else:
                return 0

    @staticmethod
    def adder(x, y):
        # return x + y
        carry = 0
        while y:
            carry = x & y
            x ^= y
            y = carry << 1
        return x

    @staticmethod
    def subtractor(x, y):
        # return x - y
        borrow = 0
        while y:
            borrow = (~x) & y
            x ^= y
            y = borrow << 1
        return x

    # @staticmethod
    # def adder(x, y):
    #     # return x + y
    #     carry = 0
    #     i = 0
    #     while y and i < 100:
    #         carry = x & y
    #         x ^= y
    #         y = carry << 1
    #         i += 1
    #     return x

    # @staticmethod
    # def subtractor(x, y):
    #     # return x - y
    #     borrow = 0
    #     i = 0
    #     while y and i < 100:
    #         borrow = (~x) & y
    #         x ^= y
    #         y = borrow << 1
    #         i += 1
    #     return x



if __name__ == '__main__':
    solu = Solution()
    # x, y = 5, -9
    # res = solu.getSum(x, y)
    xys = [(5, -9), (5, -4), (4, -3), (4, -6), (1, 3), (-3, -2)]
    for xy in xys:
        res = solu.getSum(*xy)
        print(*xy, res)