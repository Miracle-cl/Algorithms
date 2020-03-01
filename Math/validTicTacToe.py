from typing import List

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:

        def linear(board, tag):
            tags = tag * 3
            boardT = [''.join(b[j] for b in board) for j in range(3)] # arr.T
            # r1 = any(b == tags for b in board)
            # r2 = any(b == tags for b in boardT)
            # r3 = all(board[i][i] == tag for i in range(3)) or all(board[i][2-i] == tag for i in range(3))
            return any(b == tags for b in board) or any(b == tags for b in boardT) or \
                all(board[i][i] == tag for i in range(3)) or all(board[i][2-i] == tag for i in range(3))

        cx, co = 0, 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X':
                    cx += 1
                elif board[i][j] == 'O':
                    co += 1

        if co > cx or cx > co + 1:
            return False

        if co == cx:
            # if 'X' win then false
            if linear(board, 'X'):
                return False

        elif co + 1 == cx:
            # if 'O' win then false
            if linear(board, 'O'):
                return False

        return True


board = ["XXX", "   ", "OOO"]
solu = Solution()
res = solu.validTicTacToe(board)
print(res)