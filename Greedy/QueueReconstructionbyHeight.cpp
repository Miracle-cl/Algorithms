#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;


class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        std::sort(people.begin(), people.end(), 
            [](const vector<int>& u, const vector<int>& v) 
            {return u[0]>v[0] || (u[0]==v[0] && u[1]<v[1]);}
        );
        vector<vector<int>> res;
        for (auto& person : people) {
            res.insert(res.begin() + person[1], person);
        }
        return res;
    }
};

int main () 
{
    vector<vector<int>> people {{7,1}, {4,4}, {7,0}, {5,0}, {6,1}, {5,2}};
    Solution solu;
    vector<vector<int>> res = solu.reconstructQueue(people);
    for (auto& person : res)
        std::cout << person[0] << ' ' << person[1] << '\n';
    return 0;
}