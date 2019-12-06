class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        kc = [str(i) for i in range(k)]
        if n == 1:
            return ''.join(kc)
        res = []
        _mem = ['']
        x = 1-n
        first = '0' * n
        while n > 0:
            _mem = [x + str(i) for x in _mem for i in range(k)]
            n -= 1
        _mem = set(_mem)
        
        def dfs(tmp, num):
            if res:
                return
            if num==0:
                res.append(tmp)
                return
            for c in kc:
                end_str = tmp[x:] + c
                if end_str in _mem:
                    _mem.discard(end_str)
                    dfs(tmp+c, num-1)
                    _mem.add(end_str)
        
        
        _mem.discard(first)
        dfs(first, len(_mem))
        return res[0] if res else ''