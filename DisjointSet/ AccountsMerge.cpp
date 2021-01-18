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


using std::vector;
// using std::greater; // functional
// using std::unordered_set;
using std::unordered_map;
using std::pair;
using std::make_pair;
using std::string;


class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        unordered_map<string, int> mail2id;
        vector<string> names;
        vector<string> mails;
        for (auto& account : accounts) {
            for (int i = 1; i < account.size(); i++) {
                if (mail2id.count(account[i]) == 0) {
                    mail2id[account[i]] = mails.size();
                    mails.emplace_back(account[i]);
                    names.emplace_back(account[0]);
                }
            }
        }

        int lens = mails.size();
        vector<int> roots(lens, 0);
        for (int i = 1; i < lens; i ++) 
            roots[i] = i;
        for (auto& account : accounts) {
            if (account.size() < 3)
                continue;
            for (int i = 2, u = mail2id[account[1]]; i < account.size(); i++)
                merge(u, mail2id[account[i]], roots);
        }
        
        unordered_map<int, vector<string>> rid2mail;
        for (int i = 0; i < lens; i++) {
            int ri = find(i, roots);
            if (rid2mail.count(ri) == 0)
                rid2mail[ri].emplace_back(names[ri]);
            rid2mail[ri].emplace_back(mails[i]);
        }

        vector<vector<string>> res;
        // for (auto& x : rid2mail) {
        //     vector<string> tmp;
        //     tmp.emplace_back(names[x.first]);
        //     std::sort(x.second.begin(), x.second.end());
        //     for (string& s : x.second) 
        //         tmp.emplace_back(s);
        //     res.emplace_back(tmp);
        // }

        // for (auto& [rid, email] : rid2mail) {
        //     tmp.emplace_back(names[rid]);
        //     std::sort(email.begin(), email.end());
        //     for (string& s : email) 
        //         tmp.emplace_back(s);
        //     res.emplace_back(tmp);
        // }

        for (auto& [_, account] : rid2mail) {
            std::sort(account.begin() + 1, account.end());
            res.emplace_back(account);
        }
        return res;
    }
    
    int find(int x, vector<int>& roots) {
        if (x != roots[x])
            roots[x] = find(roots[x], roots);
        return roots[x];
    }

    void merge(int x, int y, vector<int>& roots) {
        int rx = find(x, roots);
        int ry = find(y, roots);
        if (rx == ry) return;
        roots[rx] = ry;
        return;
    }
};


int main () 
{
    vector<vector<string>> accounts {{"John", "johnsmith@mail.com", "john00@mail.com"}, 
            {"John", "johnnybravo@mail.com"}, 
            {"John", "johnsmith@mail.com", "john_newyork@mail.com"}, 
            {"Mary", "mary@mail.com"}};

    Solution sol;
    vector<vector<string>> ans = sol.accountsMerge(accounts);
    for (auto& acc : ans) {
        for (string& s : acc) {
            // printf("%s, ", s);
            std::cout << s << ' ';
        }
        std::cout << '\n';
    }
    return 0;
}
