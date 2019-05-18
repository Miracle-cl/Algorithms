#include <iostream>
#include <vector>
#include <stack>

using std::vector;
using std::stack;

class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if (matrix.empty() || matrix[0].empty())
            return 0;
        int row = matrix.size();
        int column = matrix[0].size();
        int max_area = 0;
        vector<int> prev(column, 0);
        vector<int> height(column, 0);
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                int tmp = ((matrix[i][j] == '1') ? 1 : 0);
                height[j] = tmp == 0 ? 0 : (prev[j] + tmp);
            }
            max_area = std::max(max_area, LargestRectangleInHistogram(height));
            prev = height;
            // print_vector(height);
            // print_vector(prev);
        }
        return max_area;
    }

    int LargestRectangleInHistogram(vector<int> heights) {
        heights.push_back(0);
        stack<int> stk;
        int i = 0, max_area = 0;
        while (i < heights.size()) {
            if (stk.empty() || heights[i] > heights[stk.top()]) {
                stk.push(i++);
            }
            else {
                int tmp = stk.top();
                stk.pop();
                max_area = std::max(max_area, heights[tmp] * (stk.empty() ? i : (i - stk.top() - 1)));
            }
        }
        return max_area;
    }

    void print_vector(const vector<int>& vs) {
        for (auto x : vs) {
            std::cout << x << "  ";
        }
        std::cout << "\n";
    }
};


class Solution2 {
// hard
public:
    void print_vector(const vector<int>& vs) {
        for (auto x : vs) {
            std::cout << x << "  ";
        }
        std::cout << "\n";
    }

    int maximalRectangle(vector<vector<char> > &matrix) {
        if (matrix.empty()) return 0;
        const int m = matrix.size();
        const int n = matrix[0].size();
        vector<int> H(n, 0);
        vector<int> L(n, 0);
        vector<int> R(n, n);
        int ret = 0;
        for (int i = 0; i < m; ++i) {
            int left = 0, right = n;
            // calculate L(i, j) from left to right
            for (int j = 0; j < n; ++j) {
                if (matrix[i][j] == '1') {
                    ++H[j];
                    L[j] = std::max(L[j], left);
                }
                else {
                    left = j+1;
                    H[j] = 0;
                    L[j] = 0;
                    R[j] = n;
                }
            }
            // calculate R(i, j) from right to left
            for (int j = n-1; j >= 0; --j) {
                if (matrix[i][j] == '1') {
                    R[j] = std::min(R[j], right);
                    ret = std::max(ret, H[j]*(R[j]-L[j]));
                }
                else {
                    right = j;
                }
            }

            print_vector(H);
            print_vector(L);
            print_vector(R);
            std::cout << "\n";
        }
        return ret;
    }
};

int main()
{
    // vector<vector<char>> matrix {{'1','0','1','0','0'},
    //                              {'1','0','1','1','1'},
    //                              {'1','1','1','1','1'},
    //                              {'1','0','0','1','0'}};
    vector<vector<char>> matrix {{'1', '0'}, {'0', '1'}};
    // vector<int> v {2,1,5,6,2,3};
    Solution solu;
    // int res = solu.LargestRectangleInHistogram(v);
    int res = solu.maximalRectangle(matrix);
    std::cout << res << "\n";
    return 0;
}

// matrix
// [
//   ["1","0","1","0","0"], --- 10100
//   ["1","0","1","1","1"], --- 20211
//   ["1","1","1","1","1"], --- 31322
//   ["1","0","0","1","0"]  --- 40030
// ]
