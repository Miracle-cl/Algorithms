class Solution:
    def longestDupSubstring(self, S: str) -> str:
        nums =[ord(c) - ord('a') for c in S]
        N = len(nums)
        l, r = 0, N
        mode = int(1e9 + 7) # mode = 2**63 - 1

        def search(lens):
            h = 0 # hash value
            for i in range(lens):
                h = (h * 26 + nums[i]) % mode

            h_map = {h: 0}
            al = pow(26, lens, mode)
            for i in range(1, N - lens + 1):
                h = (h * 26 - nums[i-1] * al + nums[i+lens-1]) % mode
                if h in h_map:
                    sid = h_map[h]
                    # same hash value but not same string, (little bug) -> someone changes mode = 2**63 - 1
                    if S[sid:sid+lens] == S[i:i+lens]:
                        return i
                h_map[h] = i
            return -1

        begin = 0
        while l < r:
            mid = (l + r) // 2
            pos = search(mid)
            if pos > -1:
                l = mid + 1
                begin = pos
            else:
                r = mid
        print(begin, l)
        return S[begin: begin+l-1]

ss = Solution()
S = 'bananaxx'
# S = 'abcd'
res = ss.longestDupSubstring(S)
print([res])