class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        pre = self.kthGrammar(N-1, (K+1)//2)
        return (K+1+pre) % 2
        # if pre:
        #     return K % 2
        # else:
        #     return (K+1) % 2
        
solu = Solution()
solu.kthGrammar(2,2)