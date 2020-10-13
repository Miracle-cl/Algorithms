#include <iostream>
#include <vector>
#include <stack>
#include <string>
#include <tuple> 
// #include <queue>

using std::stack;
using std::vector;
using std::pair;
using std::string;
using std::tuple;


class Solution {
public:
    vector<int> exclusiveTime_c(int n, vector<string>& logs) {
        int id, time, prev;
        char tag[6];
        stack<int> stk;
        vector<int> res(n, 0);
        for (const string& s : logs) {
            sscanf(s.c_str(), "%d:%[a-z]:%d", &id, tag, &time);
            if (tag[0] == 's') {
                if (!stk.empty())
                    res[stk.top()] += time - prev;
                stk.push(id);
                prev = time;
            }
            else {
                res[id] += time + 1 - prev;
                stk.pop();
                prev = time + 1;
            }
        }
        return res;
    }

    vector<int> exclusiveTime(int n, vector<string>& logs) {
        int id, time, prev;
        char tag;
        stack<int> stk;
        vector<int> res(n, 0);
        for (const string& s : logs) {
            auto p = parse_str(s);
            std::tie(id, time, tag) = p;
            if (tag == 's') {
                if (!stk.empty())
                    res[stk.top()] += time - prev;
                stk.push(id);
                prev = time;
            }
            else {
                res[id] += time + 1 - prev;
                stk.pop();
                prev = time + 1;
            }
        }
        return res;
    }

    tuple<int, int, char> parse_str(string s) {
        int i = s.find_first_of(":");
        int j = s.find_last_of(":");
        string x = s.substr(0, i);
        string y = s.substr(j+1, s.size()-j-1);
        char tag = s[i+1];
        // pair<int, int> res {std::stoi(x), std::stoi(y)};
        // pair<int, int> res(std::stoi(x), std::stoi(y));
        return {std::stoi(x), std::stoi(y), tag};
    }

    // pair<int, int> find_time(string s) {
    //     int i = s.find_first_of(":");
    //     int j = s.find_last_of(":");
    //     string x = s.substr(0, i);
    //     string y = s.substr(j+1, s.size()-j-1);
    //     // pair<int, int> res {std::stoi(x), std::stoi(y)};
    //     // pair<int, int> res(std::stoi(x), std::stoi(y));
    //     return {std::stoi(x), std::stoi(y)};
    // }
};


int main()
{
    int n = 2;
    vector<string> logs{"0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"};
    Solution solu;
    // vector<int> res = solu.exclusiveTime_c(n, logs);
    vector<int> res = solu.exclusiveTime(n, logs);
    // string s("0:end:6");
    // tuple<int, int, char> p = solu.parse_str(s);
    // std::cout << std::get<0>(p) << '\n';
    std::cout << res[0] << '\n';
    std::cout << res[1] << '\n';
    return 0;
}