#include <iostream>
#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
public:
    struct TrieNode {
        TrieNode *child[26];
        string str;
        TrieNode() : str("") {
            for (auto &a : child)
                a = NULL;
        }
    };

    struct Trie {
        TrieNode *root;
        Trie() : root(new TrieNode()) {}

        void insert(string s) {
            TrieNode *p = root;
            for (auto &a : s) {
                int i = a - 'a';
                if (!p->child[i])
                    p->child[i] = new TrieNode();
                p = p->child[i];
            }
            p->str = s;
        }
    };

    void viewTrie(vector<string>& words) {
        Trie T;
        for (auto &a : words)
            T.insert(a);
        if (T.root->child[5])
            std::cout << "have node\n";
        else
            std::cout << "no node\n";
        std::cout << T.root->child[4]->child[0]->child[19]->str << '\n';
    }

    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        vector<string> res;
        if (words.empty() || board.empty() || board[0].empty())
            return res;

        int row = board.size();
        int col = board[0].size();
        vector<vector<bool>> visited(row, vector<bool>(col, false));
        Trie T;
        for (auto &a : words)
            T.insert(a);

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (T.root->child[board[i][j] - 'a']) {
                    dfs(i, j, row, col, T.root->child[board[i][j] - 'a'], board, visited, res);
                }
            }
        }
        return res;
    }

    void dfs(int r, int c, const int row, const int col, TrieNode *p, const vector<vector<char>>& board,
             vector<vector<bool>>& visited, vector<string>& res) {
        if (!p->str.empty()) {
            res.push_back(p->str);
            p->str.clear();
        }
        visited[r][c] = true;
        int d[][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (auto &item : d) {
            int nr = item[0] + r;
            int nc = item[1] + c;
            if (nr >= 0 && nr < row && nc >= 0 && nc < col && (!visited[nr][nc]) && p->child[board[nr][nc] - 'a']) {
                dfs(nr, nc, row, col, p->child[board[nr][nc] - 'a'], board, visited, res);
            }
        }
        visited[r][c] = false;
    }
};

int main()
{
    // vector<vector<char>> board = {{'o','a','a','n'},
    //                               {'e','t','a','e'},
    //                               {'i','h','k','r'},
    //                               {'i','f','l','v'}};
    // vector<string> words = {"oath","pea","eat","rain"};
    vector<vector<char>> board = {{'a','a'}};
    vector<string> words = {"a"};
    Solution solu;
    // solu.viewTrie(words);
    // std::cout << ('t' - 'a') << "\n";
    vector<string> res = solu.findWords(board, words);
    for (auto str : res)
        std::cout << str << "\n";
    return 0;
}
