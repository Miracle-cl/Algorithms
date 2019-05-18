#include <iostream>
#include <vector>

using std::vector;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> res(2, -1);
        if (nums.empty())
            return res;
        int l = 0, r = nums.size()-1;
        int mid;
        while (l < r) {
            mid = (l + r) / 2;
            if (nums[mid] < target)
                l = mid + 1;
            else
                r = mid;
        }
        if (nums[l] != target)
            return res;
        res[0] = l;
        r = nums.size();
        while (l < r) {
            mid = (l + r) / 2;
            if (nums[mid] <= target)
                l = mid + 1;
            else
                r = mid;
        }
        res[1] = l - 1;
        return res;
    }
};

int main()
{
    vector<int> nums {5,5,7,8,8,10};
    int t = 5;
    Solution solu;
    vector<int> res = solu.searchRange(nums, t);
    std::cout << res[0] << res[1] << "\n";
    return 0;
}
