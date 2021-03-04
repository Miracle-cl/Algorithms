// board =
// [
//   ['A','B','C','E'],
//   ['S','F','C','S'],
//   ['A','D','E','E']
// ]
//
// Given word = "ABCCED", return true.
// Given word = "SEE", return true.
// Given word = "ABCB", return false.
#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>

using std::string;
using std::vector;

// class Solution {
// public:
//     bool exist(vector<vector<char>>& board, string word) {
//         int row = board.size();
//         int col = board[0].size();
//         vector<vector<bool>> visited(row, vector<bool>(col, false));
//         for (int i = 0; i < row; i++) {
//             for (int j = 0; j < col; j++) {
//                 if (dfs(i, j, 0, row, col, word, board, visited)) {
//                     return true;
//                 }
//             }
//         }
//         return false;
//     }

//     bool dfs(int r, int c, int k, const int row, const int col,
//              const string& word, const vector<vector<char>>& board, vector<vector<bool>>& visited) {
//         if (k == word.size())
//             return true;

//         if (r < 0 || c < 0 || r >= row || c >= col)
//             return false;

//         if (board[r][c] != word[k] || (visited[r][c]))
//             return false;

//         visited[r][c] = true;
//         bool ret = dfs(r-1, c, k+1, row, col, word, board, visited) ||
//                    dfs(r+1, c, k+1, row, col, word, board, visited) ||
//                    dfs(r, c-1, k+1, row, col, word, board, visited) ||
//                    dfs(r, c+1, k+1, row, col, word, board, visited);
//         visited[r][c] = false;
//         return ret;
//     }
// };

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        r = board.size(), c = board[0].size();
        n = word.size();
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (dfs(i, j, 0, board, word))
                    return true;
            }
        }
        return false;
    }
private:
    int r, c, n;
    bool dfs(int i, int j, int k, vector<vector<char>>& board, const string& word) {
        if (i < 0 || j <0 || i >= r || j >= c || word[k] != board[i][j])
            return false;
        if (k == n - 1)
            return true;
        board[i][j] = '\0';
        bool res = dfs(i-1, j, k+1, board, word) || dfs(i+1, j, k+1, board, word) ||
                dfs(i, j-1, k+1, board, word) || dfs(i, j+1, k+1, board, word);
        board[i][j] = word[k];
        return res;
    }
};

int main()
{
    // vector<vector<char>> board = {
    //                                {'A','B','C','E'},
    //                                {'S','F','C','S'},
    //                                {'A','D','E','E'}
    //                            };
    // string word ("SEE");
    // vector<vector<char>> board = {{'c', 'a', 'a'}, {'a', 'a', 'a'}, {'b', 'c', 'd'}};
    // string word ("aab");
    // Solution solu;
    // std::cout << solu.exist(board, word) << "\n";
    std::vector<string> v {"a", "v", "a"};
    std::unordered_set<string> myset(v.begin(), v.end());
    for (auto x : myset)
        std::cout << x << "\n";
    return 0;
}
