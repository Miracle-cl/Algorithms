# title: Valid Sudoku
#
# description:
# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

# Notes:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        flag = 0
        # row is valid
        for row in board:
            not_num_r = row.count('.')
            if len(set(row)) != 10 - not_num_r:
                flag = 1
                break
        if flag:
            return False
        else:
            # column is valid
            for i in range(9):
                column = []
                for j in range(9):
                    column.append( board[j][i] )
                not_num_c = column.count('.')
                if len(set(column)) != 10 - not_num_c:
                    flag = 1
                    break
            if flag:
                return False
            else:
                # subgrid is valid
                for u in [0,3,6]:
                    for v in [0,3,6]:
                        first = board[u][v]
                        subgrid = [board[u][v], board[u][v+1], board[u][v+2],
                                   board[u+1][v], board[u+1][v+1], board[u+1][v+2],
                                   board[u+2][v], board[u+2][v+1], board[u+2][v+2]]
                        not_num_s = subgrid.count('.')
                        if len(set(subgrid)) != 10 - not_num_s:
                            flag = 1
                            break
                if flag:
                    return False
                else:
                    return True
