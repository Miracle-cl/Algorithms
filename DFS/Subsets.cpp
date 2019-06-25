#include <iostream>
#include <vector>

using std::vector;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> temp;
        dfs(res, temp, nums, 0);
        return res;
    }

    void dfs(vector<vector<int>>& res, vector<int>& temp, const vector<int>& nums, int start) {
        res.push_back(temp);
        for (int i = start; i < nums.size(); i++) {
            temp.push_back(nums[i]);
            dfs(res, temp, nums, i+1);
            temp.pop_back();
        }
    }

    void print_vector(const vector<int>& vs) {
        for (auto i : vs) {
            std::cout << i << " ";
        }
        std::cout << "\n";
    }
};

int main()
{
    vector<int> n {1,2,3};
    Solution s;
    vector<vector<int>> res = s.subsets(n);
    for (auto sv : res) {
        s.print_vector(sv);
    }
    return 0;
}
