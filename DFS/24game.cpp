#include <iostream>
#include <vector>

using std::vector;
using std::pair;
using std::string;

class Solution {
public:
    bool judgePoint24(vector<int>& nums) {
        bool res = false;
        vector<double> temp(nums.begin(), nums.end());
        helperbool(temp, res);
        return res;
    }

    void helperbool(vector<double>& temp, bool& res) {
        if (res)
            return;

        if (temp.size() == 1 && abs(24 - temp[0]) < 0.001) {
            res = true;
            return;
        }

        for (int i = 0; i < temp.size(); i++) {
            for (int j = i+1; j < temp.size(); j++) {
                double p = temp[i], q = temp[j];
                vector<double> ts {p-q, q-p, p+q, p*q};
                if (p > 0.001 || -p > 0.001) ts.push_back(q/p);
                if (q > 0.001 || -q > 0.001) ts.push_back(p/q);
                temp.erase(temp.begin() + j);
                temp.erase(temp.begin() + i);
                for (auto dn : ts) {
                    temp.push_back(dn);
                    helperbool(temp, res);
                    temp.pop_back();
                }
                temp.insert(temp.begin() + i, p);
                temp.insert(temp.begin() + j, q);
            }
        }
    }

    // get all posibilities
    vector<string> getPoint24(vector<int>& nums) {
        bool res = false;
        vector<string> formula;
        vector<pair<double, string>> temp;
        for (auto n : nums)
            temp.push_back(std::make_pair(n, std::to_string(n)));
        helper(temp, res, formula);
        return formula;
    }

    vector<pair<double, string>> get_cal(pair<double, string> p1, pair<double, string> p2) {
        vector<pair<double, string>> t;
        t.push_back( {p1.first - p2.first, "(" + p1.second + "-" + p2.second + ")"} );
        t.push_back( {p1.first + p2.first, "(" + p1.second + "+" + p2.second + ")"} );
        t.push_back( {p1.first * p2.first, "(" + p1.second + "*" + p2.second + ")"} );
        t.push_back( {p2.first - p1.first, "(" + p2.second + "-" + p1.second + ")"} );
        if (p1.first > 0.001 || -p1.first > 0.001)
            t.push_back( {p2.first / p1.first, "(" + p2.second + "/" + p1.second + ")"} );
        if (p2.first > 0.001 || -p2.first > 0.001)
            t.push_back( {p1.first / p2.first, "(" + p1.second + "/" + p2.second + ")"} );
        return t;
    }

    void helper(vector<pair<double, string>>& temp, bool& res, vector<string>& formula) {
        // if (res)
        //     return;

        if (temp.size() == 1 && abs(24 - temp[0].first) < 0.001) {
            res = true;
            // std::cout << temp[0].second << "\n";
            formula.push_back(temp[0].second);
            return;
        }

        for (int i = 0; i < temp.size(); i++) {
            for (int j = i+1; j < temp.size(); j++) {
                pair<double, string> p = temp[i];
                pair<double, string> q = temp[j];
                vector<pair<double, string>> ts = get_cal(p, q);
                temp.erase(temp.begin() + j);
                temp.erase(temp.begin() + i);
                for (auto dn : ts) {
                    temp.push_back(dn);
                    helper(temp, res, formula);
                    temp.pop_back();
                }
                temp.insert(temp.begin() + i, p);
                temp.insert(temp.begin() + j, q);
            }
        }
    }
};

int main()
{
    vector<int> nums {8,1,3,2};
    // vector<int> nums {8,8,3,3};
    Solution s;
    vector<string> formula = s.getPoint24(nums);
    for (auto s : formula)
        std::cout << s << "\n";
    return 0;
}
