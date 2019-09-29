class SolutionBFS:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ## a little faster than dfs in this case
        # 116ms, 14.2MB
        if len(board) < 3 or len(board[0]) < 3:
            return
        r, c = len(board), len(board[0])
        for j in range(c-1):
            self._bfs(0, j, r, c, board)
        for i in range(r-1):
            self._bfs(i, c-1, r, c, board)
        for j in range(1, c):
            self._bfs(r-1, j, r, c, board)
        for i in range(1, r):
            self._bfs(i, 0, r, c, board)

        for i in range(r):
            for j in range(c):
                if board[i][j] == '$':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        # print(board)

    def _bfs(self, i, j, r, c, board):
        if board[i][j] != 'O':
            return
        q = [(i, j)]
        board[i][j] = '$'
        while q:
            x, y = q.pop(0)
            if x > 0 and board[x-1][y] == 'O':
                q.append((x-1, y))
                board[x-1][y] = '$'
            if x + 1 < r and board[x+1][y] == 'O':
                q.append((x+1, y))
                board[x+1][y] = '$'
            if y > 0 and board[x][y-1] == 'O':
                q.append((x, y-1))
                board[x][y-1] = '$'
            if y + 1 < c and board[x][y+1] == 'O':
                q.append((x, y+1))
                board[x][y+1] = '$'
        return


class SolutionDFS:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 124ms, 14.9MB
        if len(board) < 3 or len(board[0]) < 3:
            return
        r, c = len(board), len(board[0])
        for j in range(c-1):
            self._dfs(0, j, r, c, board)
        for i in range(r-1):
            self._dfs(i, c-1, r, c, board)
        for j in range(1, c):
            self._dfs(r-1, j, r, c, board)
        for i in range(1, r):
            self._dfs(i, 0, r, c, board)

        for i in range(r):
            for j in range(c):
                if board[i][j] == '$':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        # print(board)

    def _dfs(self, i, j, r, c, board):
        if i < 0 or i >= r or j < 0 or j >= c or board[i][j] != 'O':
            return
        board[i][j] = '$'
        self._dfs(i-1, j, r, c, board)
        self._dfs(i+1, j, r, c, board)
        self._dfs(i, j-1, r, c, board)
        self._dfs(i, j+1, r, c, board)


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
