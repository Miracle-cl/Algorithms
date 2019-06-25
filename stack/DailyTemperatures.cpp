#include <iostream>
#include <vector>
#include <stack>

using std::vector;
using std::stack;

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        vector<int> days(T.size());
        stack<int> stk;
        for (int i = T.size()-1; i >= 0; i--) {
            while (!stk.empty() and T[stk.top()] <= T[i])
                stk.pop();
            days[i] = stk.empty() ? 0 : stk.top() - i;
            stk.push(i);
        }
        return days;
    }
};

int main()
{
    vector<int> T {73, 74, 75, 71, 69, 72, 76, 73};
    // output : 1, 1, 4, 2, 1, 1, 0, 0
    Solution s;
    vector<int> days = s.dailyTemperatures(T);
    for (auto n: days) {
        std::cout << n << " ";
    }
    std::cout << "\n";
    return 0;
}

// python3
// class Solution:
//     def dailyTemperatures(self, T: List[int]) -> List[int]:
//         days = [0 for _ in T]
//         stk = list()
//         for i in range(len(T)-1, -1, -1):
//             while stk and T[stk[-1]] <= T[i]:
//                 stk.pop()
//             days[i] = stk[-1] - i if stk else 0
//             stk.append(i)
//         return days
