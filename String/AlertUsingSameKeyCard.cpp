#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
#include <algorithm>

using std::vector;
using std::unordered_map;
using std::string;


class Solution {
public:
    vector<string> alertNames(vector<string>& keyName, vector<string>& keyTime) {
        int h, m;
        unordered_map<string, vector<int>> n2t;
        for (int i = 0; i < keyName.size(); i++) {
            // string name = keyName[i];
            sscanf(keyTime[i].c_str(), "%d:%d", &h, &m);
            n2t[keyName[i]].emplace_back(h * 60 + m);
        }
        vector<string> names;
        for (auto p : n2t) {
            int n = p.second.size();
            if (n < 3)
                continue;
            sort(p.second.begin(), p.second.end());
            for (int i = 2; i < n; i++) {
                if (p.second[i] - p.second[i-2] <= 60) {
                    names.emplace_back(p.first);
                    break;
                }
            }
        }
        sort(names.begin(), names.end());
        return names;
    }
};



int main()
{
    vector<string> keyName {"daniel","daniel","daniel","luis","luis","luis","luis"};
    vector<string> keyTime {"10:00","10:40","11:00","09:00","11:00","13:00","15:00"};
    // vector<string> keyName {"leslie","leslie","leslie","clare","clare","clare","clare"};
    // vector<string> keyTime {"13:00","13:20","14:00","18:00","18:51","19:30","19:49"};
    Solution solu;
    vector<string> res = solu.alertNames(keyName, keyTime);
    for (string s : res)
        std::cout << s << ' ';
    std::cout << '\n';
    return 0;
}


// class Solution {
// public:
//     vector<string> alertNames(vector<string>& keyName, vector<string>& keyTime) {
//         int n = keyName.size();
//         unordered_map<string, vector<int>> s;
        
//         auto enc = [](const string& s) {
//             string u = s.substr(0, 2);
//             string v = s.substr(3, 2);
//             return stoi(u) * 60 + stoi(v); //时间统一换成s单位来表示
//         };
        
//         for (int i = 0; i < n; ++i) {
//             s[keyName[i]].push_back(enc(keyTime[i]));
//         }
        
//         vector<string> ans;
//         for (auto&& [k, v]: s) {
//             sort(v.begin(), v.end());
//             if (v.size() > 2) {
//                 for (int i = 2; i < v.size(); ++i) {
//                     if (v[i] - v[i - 2] <= 60) {
//                         ans.push_back(k);
//                         break;
//                     }
//                 }
//             }
//         }
        
//         sort(ans.begin(), ans.end());
//         return ans;
//     }
// };