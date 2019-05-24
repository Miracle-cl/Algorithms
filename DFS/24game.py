class Solution:
    def judgePoint24(self, nums):
        self.res = False
        self.nums = [[n, str(n)] for n in nums]
        self.dfs()
        return self.res

    def get_formula(self, s1, s2, op):
        return "({})".format(s1 + op + s2)

    def dfs(self):
        # if self.res:
        #     return
        if len(self.nums) == 1 and abs(self.nums[0][0] - 24) < 0.001:
            self.res = True
            print(self.nums[0][1])
            return
        for i in range(len(self.nums)):
            for j in range(i+1, len(self.nums)):
                q, qs = self.nums.pop(j)
                p, ps = self.nums.pop(i)
                # temp = [p-q, q-p, p+q, p*q]
                temp = [[p-q, self.get_formula(ps, qs, '-')],
                        [q-p, self.get_formula(qs, ps, '-')],
                        [p+q, self.get_formula(ps, qs, '+')],
                        [p*q, self.get_formula(ps, qs, '*')]]
                if p != 0:
                    temp.append([q/p, self.get_formula(qs, ps, '/')])
                if q != 0:
                    temp.append([p/q, self.get_formula(ps, qs, '/')])
                for n in temp:
                    self.nums.append(n)
                    self.dfs()
                    self.nums.pop()
                self.nums.insert(i, [p, ps])
                self.nums.insert(j, [q, qs])

if __name__ == "__main__":
    # nums = [4,1,3,3]
    # nums = [8,8,3,3]
    nums = [8,1,3,2]
    s = Solution()
    res = s.judgePoint24(nums)
    print(res)
