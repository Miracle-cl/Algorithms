#include <iostream>
#include <stack>
#include <vector>

using std::stack;
using std::vector;

class Solution {
public:
    int largestRectangleArea(vector<int>& height) {
        stack<int> s;
        int result = 0;
        height.push_back(0);
        for (int i = 0; i < height.size(); ) {
            if (s.empty() || height[i] > height[s.top()])
                s.push(i++);
            else {
                int tmp = s.top();
                s.pop();
                result = std::max(result, height[tmp] * (s.empty() ? i : (i - s.top() - 1)));
            }
        }
        return result;
    }
};

int main()
{
    vector<int> s {2,1,5,6,6,6};
    Solution solu;
    std::cout << solu.largestRectangleArea(s) << "\n";
    return 0;
}
