class Trie:
    def __init__(self):
        self.root = {}
        self.end = -1

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        # node[self.end] = True
        node[self.end] = word

    def search(self, word):
        curNode = self.root
        for c in word:
            if c not in curNode:
                return False
            curNode = curNode[c]

        # Doesn't end here
        if self.end not in curNode:
            return False
        return True

class Solution:
    def findWords(self, board, words):
        self.board = board
        self.tt = Trie()
        for word in words:
            self.tt.insert(word)
        self.res = []
        self.row, self.col = len(board), len(board[0])
        self.moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        self.visited = [[False] * self.col for _ in range(self.row)]
        for r in range(self.row):
            for c in range(self.col):
                if board[r][c] in self.tt.root:
                    self.dfs(r, c, self.tt.root[board[r][c]])
        return list(set(self.res))

    def dfs(self, r, c, node):
        # node is dict
        if (-1 in node):
            self.res.append(node[-1])

        self.visited[r][c] = True

        for move in self.moves:
            nr, nc = r + move[0], c + move[1]
            if (nr >= 0 and
                nc >= 0 and
                nr < self.row and
                nc < self.col and
                (not self.visited[nr][nc]) and
                self.board[nr][nc] in node):

                self.dfs(nr, nc, node[ self.board[nr][nc] ])

        self.visited[r][c] = False


# board = [['o','a','a','n'],
#           ['e','t','a','e'],
#           ['i','h','k','r'],
#           ['i','f','l','v']]
# words = ["oath","pea","eat","rain"]
board = [['a', 'a']]
words = ['a']

ss = Solution()
print(ss.findWords(board, words))
# tt = Trie()
# for word in words:
#     tt.insert(word)
# print(tt.root['o'])
