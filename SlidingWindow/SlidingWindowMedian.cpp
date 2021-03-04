#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;



class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        vector<int> windows(nums.begin(), nums.begin() + k);
        std::sort(windows.begin(), windows.end());
        vector<int>::iterator it;
        vector<double> ans;
        for (int i = k; i < nums.size(); i++) {
            double median = ((double) windows[k/2] + windows[(k-1)/2]) / 2.0;
            ans.emplace_back(median);
            it = std::upper_bound(windows.begin(), windows.end(), nums[i-k]);
            windows.erase(it-1);
            it = std::upper_bound(windows.begin(), windows.end(), nums[i]);
            windows.insert(it, nums[i]);
        }
        double median = ((double) windows[k/2] + windows[(k-1)/2]) / 2.0;
        ans.emplace_back(median);
        return ans;
    }

    vector<double> medianSlidingWindow_1(vector<int>& nums, int k) {
        vector<int> windows(nums.begin(), nums.begin() + k);
        std::sort(windows.begin(), windows.end());
        // vector<int>::iterator it;
        vector<double> ans;
        for (int i = k; i < nums.size(); i++) {
            double median = (windows[k/2] + windows[(k-1)/2]) / 2.0;
            ans.emplace_back(median);
            windows.push_back(nums[i]);
            auto it = std::prev(windows.end(), 1); // windows.end() - 1
            auto const insert_it = std::upper_bound(windows.begin(), it, nums[i]);
            std::rotate(insert_it, it, it+1);
            windows.erase(std::lower_bound(windows.begin(), windows.end(), nums[i-k]));
        }
        double median = (windows[k/2] + windows[(k-1)/2]) / 2.0;
        ans.emplace_back(median);
        for (double x : ans) 
            std::cout << x << ' ';
        std::cout << '\n';
        return ans;
    }
};


int main () 
{
    vector<int> nums {1,3,-1,-3,5,3,6,7};
    int k = 3;
    Solution sol;
    vector<double> res = sol.medianSlidingWindow(nums, k);
    for (double x : res) 
        std::cout << x << ' ';
    std::cout << '\n';
    return 0;
}