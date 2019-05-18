#include <iostream>
#include <vector>
#include <string>
#include <stdlib.h>

using std::string;
using std::vector;


vector<vector<string>> solveNQueens(int n) {
    vector<vector<string>> res;
    // vector<string> temp;
    vector<int> loc(n, -1);

}

void dfs(int start, int n, vector<vector<string>> & res,  vector<int> & loc) {
    if (start == n) {
        pa
    }
    else {
        for (int i = start; i < n; i++) {
            for (int j = 0; j < start, j++) {

            }
            if loc[i] == loc[j] || abs(loc[i] - loc[j]) == abs(i - j)
        }
    }
}

int main()
{
    int n = 4;
    std::cout << abs(4-5) << "\n";
    return 0;
}
