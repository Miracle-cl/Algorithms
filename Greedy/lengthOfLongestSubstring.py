class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        maxlen = 0
        begin = -1
        for i, c in enumerate(s):
            if c in visited and begin < visited[c]:
                begin = visited[c]
            else:
                maxlen = max(maxlen, i-begin)
            visited[c] = i
        return maxlen

if __name__ == "__main__":
    s1 = "abcabcbb" # 3
    s2 = "bbbb" # 1
    s3 = "pwwkew" # 3
    s4 = "dvdf"
    solu = Solution()
    r1 = solu.lengthOfLongestSubstring(s1)
    print(r1)
