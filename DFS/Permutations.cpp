#include <iostream>
#include <vector>
#include <algorithm> //std::find()

using std::vector;

class Solution {
public:
    // distinct integers
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> rvec;
        vector<int> temp;
        // std::sort(nums.begin(), nums.end());
        backtrack(rvec, temp, nums);
        return rvec;
    }

    void backtrack(vector<vector<int>>& rvec, vector<int>& temp, const vector<int>& nums) {
        if (temp.size() == nums.size())
            rvec.push_back(temp);
        else {
            for (int i = 0; i < nums.size(); i++) {
                if (std::find(temp.begin(), temp.end(), nums[i]) == temp.end()) {
                    temp.push_back(nums[i]);
                    backtrack(rvec, temp, nums);
                    temp.pop_back();
                }
            }
        }
    }

    // nums with duplicates
    vector<vector<int>> permuteII(vector<int>& nums) {
        vector<vector<int>> rvec;
        vector<int> temp;
        vector<bool> used(nums.size(), false); // == vector<bool> used(nums.size())
        std::sort(nums.begin(), nums.end());
        backtrack2(rvec, temp, used, nums);
        return rvec;
    }

    void backtrack2(vector<vector<int>>& rvec, vector<int>& temp, vector<bool>& used, const vector<int>& nums) {
        if (temp.size() == nums.size())
            rvec.push_back(temp);
        else {
            for (int i = 0; i < nums.size(); i++) {
                if ((used[i]) || (i > 0 && nums[i-1] == nums[i] && !used[i-1])) // ! > && > ||
                    continue;
                temp.push_back(nums[i]);
                // print_vector(temp);
                used[i] = true;
                backtrack2(rvec, temp, used, nums);
                temp.pop_back();
                // print_vector(temp);
                used[i] = false;
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
    vector<int> n {2,2,1};
    Solution solu;
    vector<vector<int>> res = solu.permuteII(n);
    for (auto x : res) {
        solu.print_vector(x);
    }
    return 0;
}
