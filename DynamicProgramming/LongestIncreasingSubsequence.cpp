#include <iostream>
#include <vector>

using std::vector;

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        if (n < 2) return n;
        vector<int> dp(n, 1);
        int max_len = 0;
        for (int j = 1; j < n; j++) {
            for (int i = 0; i < j; i++) {
                if (nums[j] > nums[i]) {
                    dp[j] = std::max(dp[i] + 1, dp[j]);
                }
            }
            if (max_len < dp[j]) max_len = dp[j];
        }
        for (auto x: dp)
            std::cout << x << " ";
        std::cout << "\n";
        return max_len;
    }
};

int main()
{
    Solution solu;
    vector<int> nums {1,3,6,7,9,4,10,5,6};
    int res = solu.lengthOfLIS(nums);
    std::cout << res << "\n";
    return 0;
}
