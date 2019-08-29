class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Manacher's Algorithm 马拉车算法 Time: O(n), Space: O(n)"""
        if len(s) < 2:
            return s
        # 预处理字符串
        ss = '#' + "#".join(list(s)) + '#'
        print(ss)
        length = len(ss)
        rightSide, rightSideCenter = 0, 0 # 右边界, 右边界对应的回文串中心
        halfLenArr = [0] * length # 保存以每个字符为中心的回文长度一半（向下取整）
        center = 0 # 记录回文中心
        longestHalf = 0 # 记录最长回文长度
        for i in range(length):
            needCalc = True # 是否需要中心扩展
            if rightSide > i: # 如果在右边界的覆盖之内
                leftCenter = 2 * rightSideCenter - i # 计算相对rightSideCenter的对称位置
                halfLenArr[i] = halfLenArr[leftCenter] # 根据回文性质得到的结论
                if i + halfLenArr[i] > rightSide: # 如果超过了右边界，进行调整
                    halfLenArr[i] = rightSide - i
                # 如果根据已知条件计算得出的最长回文小于右边界，则不需要扩展了
                if i + halfLenArr[leftCenter] < rightSide:
                    needCalc = False # 直接推出结论
            if needCalc: # 中心扩展
                while i - 1 - halfLenArr[i] >= 0 and i + 1 + halfLenArr[i] < length:
                    if ss[i + 1 + halfLenArr[i]] == ss[i - 1 - halfLenArr[i]]:
                        halfLenArr[i] += 1
                    else:
                        break
                rightSide = i + halfLenArr[i] # 更新右边界及中心
                rightSideCenter = i
                # 记录最长回文串
                if halfLenArr[i] > longestHalf:
                    center = i
                    longestHalf = halfLenArr[i]

        print(center - longestHalf + 1, center + longestHalf)
        res = [ss[i] for i in range(center - longestHalf + 1, center + longestHalf + 1, 2)]
        return "".join(res)


solu = Solution()
s = "ab"
res = solu.longestPalindrome(s)
print(res)
