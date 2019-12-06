class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        if not S:
            return ''
        cnt = 0
        vs = []
        j = 0
        for i, char in enumerate(S):
            if char == '1':
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                vs.append('1' + self.makeLargestSpecial(S[j+1 : i]) + '0')
                j = i+1
        vs.sort(reverse=True)
        return ''.join(vs)

if __name__ == '__main__':
    solu = Solution()
    s = '11011000'
    rs = solu.makeLargestSpecial(s)
    print(rs)
