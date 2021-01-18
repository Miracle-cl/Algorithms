#include <iostream>
#include <vector>
// #include <unordered_set>
#include <unordered_map>
#include <stack>
// #include <string>
// #include <tuple> 
#include <queue>
#include <deque>
// #include <functional>
#include <algorithm>

using std::stack;
using std::vector;
using std::queue;
using std::priority_queue;
using std::deque;
using std::greater; // functional
// using std::unordered_set;
using std::unordered_map;
using std::pair;
using std::make_pair;
using std::string;

// using std::tuple;


// minHeap: priority_queue <int,vector<int>,greater<int>> q; 
// maxHeap: priority_queue <int,vector<int>,less<int> >q;

class Solution {
public:
    int maximumGain(string s, int x, int y) {
        char a = 'a', b = 'b';
        if (x > y) {
            std::swap(a, b);
            std::swap(x, y);
        } // make sure x < y

        stack<char> stk, ttk;
        int score = 0;
        // drop ba
        for (char ch : s) {
            if (ch == a && !stk.empty() && stk.top() == b) {
                score += y;
                stk.pop();
            }
            else 
                stk.emplace(ch);
        }
        
        // drop ab
        while (!stk.empty()) {
            char ch = stk.top();
            stk.pop();
            if (ch == a && !ttk.empty() && ttk.top() == b) {
                score += x;
                ttk.pop();
            }
            else 
                ttk.emplace(ch);
        }
        return score;
    }
};

int main () 
{
    string s ("cdbcbbaaabab");
    int x = 4, y = 5;

    Solution sol;
    int score = sol.maximumGain(s, x, y);
    printf("%c : %d\n", 'a', score);
    return 0;
}
