#include <iostream>
#include <vector>
#include <algorithm> //std::sort

using std::vector;

class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> temp;
        std::sort(nums.begin(), nums.end());
        dfs(res, temp, nums, 0);
        return res;
    }

    void dfs(vector<vector<int>>& res, vector<int>& temp, const vector<int>& nums,
             int start) {
        res.push_back(temp);
        for (int i = start; i < nums.size(); i++) {
            if (i == start || nums[i] != nums[i-1]) {
                temp.push_back(nums[i]);
                dfs(res, temp, nums, i+1);
                temp.pop_back();
            }
        }
    }

    void print_vector(const vector<int>& vs) {
        for (auto i : vs) {
            std::cout << i << "  ";
        }
        std::cout << "\n";
    }
};

int main()
{
    vector<int> n {1,2,2};
    Solution s;
    vector<vector<int>> res = s.subsetsWithDup(n);
    for (auto sv : res) {
        s.print_vector(sv);
    }
    return 0;
}
