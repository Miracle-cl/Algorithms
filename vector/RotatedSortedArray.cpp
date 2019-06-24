#include <iostream>
#include <vector>

using std::vector;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size();
        int mid;
        while (left < right) {
            mid = (left + right) / 2;
            if (nums[mid] == target) return mid;
            if (nums[left] <= nums[mid]) {
                if (nums[mid] > target && nums[left] <= target)
                    right = mid;
                else
                    left = mid + 1;
            }
            else {
                if (nums[mid] < target && nums[right-1] >= target)
                    left = mid + 1;
                else
                    right = mid;
            }
        }
        return -1;
    }
};

int main()
{
    Solution s;
    std::vector<int> v {4,5,6,7,0,1,2};
    int t = 7;
    int res = s.search(v, t);
    std::cout << res << "\n";
    return 0;
}
