#include <iostream>
#include <string>
#include <vector>
#include <stack>

using std::string;
using std::vector;
using std::stack;

class Solution {
public:
    int evalRPN_stack(vector<string>& tokens) {
        stack<int> stk;
        int left, right;
        for (auto token : tokens) {
            if (token == "+" || token == "-" || token == "*" || token == "/") {
                right = stk.top();
                stk.pop();
                left = stk.top();
                stk.pop();
                if (token == "+")
                    stk.push(left + right);
                else if (token == "-")
                    stk.push(left - right);
                else if (token == "*")
                    stk.push(left * right);
                else
                    stk.push(left / right);
            }
            else {
                stk.push(std::stoi(token));
            }
        }
        return stk.top();
    }

    int evalRPN(vector<string>& tokens) {
        int x, y;
        string token = tokens.back();
        tokens.pop_back();
        if (is_operator(token)) {
            x = evalRPN(tokens);
            y = evalRPN(tokens);
            if (token == "+")
                y += x;
            else if (token == "-")
                y -= x;
            else if (token == "*")
                y *= x;
            else
                y /= x;
        }
        else {
            y = std::stoi(token);
        }
        return y;
    }
    
private:
    bool is_operator(const string& op) {
        return op.size() == 1 && string("+-*/").find(op) != string::npos;
    }
};

int main()
{
    vector<string> t1 {"2", "1", "+", "3", "*"};
    Solution solu;
    std::cout << solu.evalRPN_stack(t1) << "\n";
    std::cout << solu.evalRPN(t1) << "\n";
    return 0;
}
