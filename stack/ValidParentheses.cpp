#include <iostream>
#include <string>
#include <stack>

using std::string;
using std::stack;

class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        string left = "([{";
        string right = ")]}";
        for (int i = 0; i < s.size(); i++) {
            if (left.find(s[i]) != string::npos)
                stk.push(s[i]);
            else {
                if ( stk.empty() || stk.top() != left[right.find(s[i])] )
                    return false;
                else
                    stk.pop();
            }
        }
        return stk.empty();
    }
};

int main()
{
    string str ("()[{}]");
    Solution s;
    std::cout << s.isValid(str) << '\n';
    return 0;
}
