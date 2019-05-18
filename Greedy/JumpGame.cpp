#include <iostream>
#include <vector>

using std::vector;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int reach = 1;
        for (int i = 0; i < reach && reach <= nums.size(); i++) {
            reach = std::max(reach, nums[i]+i+1);
        }
        return reach >= nums.size();
    }

    int jump(vector<int>& nums) {
        int prev = -1, step = 0, cur = 0, i = 0;
        while (cur < nums.size()-1) {
            step++;
            prev = cur;
            while (i <= prev) {
                cur = std::max(cur, i + nums[i]);
                i++;
            }
            if (prev == cur)
                return -1;
        }
        return step;
    }
};

int main()
{
    // vector<int> nums {3,2,1,1,4};
    // vector<int> nums {3,2,1,0,4};
    // vector<int> nums {0,4};
    vector<int> nums {7,0,9,6,9,6,1,7,9,0,1,2,9,0,3};
    Solution s;
    std::cout << s.jump(nums) << std::endl;
    return 0;
}
