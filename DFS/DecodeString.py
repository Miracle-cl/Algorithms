class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0
        res = self.recursive(s)
        return res

    def recursive(self, s):
        res = ''
        while self.i < len(s) and s[self.i] != ']':
            if not s[self.i].isdigit():
                res += s[self.i]
                self.i += 1
            else:
                num = ''
                while self.i < len(s) and s[self.i].isdigit():
                    num += s[self.i]
                    self.i += 1
                self.i += 1
                res += self.recursive(s) * int(num)
                self.i += 1
        return res


if __name__ == '__main__':
    # s = "d3[a]2[bc]"
    s = 'd3[a2[c]]'
    # s = "2[abc]3[cd]ef"
    s = "3[a]2[b4[F]c]"
    s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
    solu = Solution()
    res = solu.decodeString(s)
    print(res)


# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".