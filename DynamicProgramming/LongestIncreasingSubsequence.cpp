#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;

// N2
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


// NlgN
class Solution1s {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> seqs;
        for (int num : nums) {
            if (seqs.empty() || seqs.back() < num) 
                seqs.emplace_back(num);
            else {
                // int i = std::lower_bound(seqs.begin(), seqs.end(), num) - seqs.begin();
                int i = bisect_left(seqs, num);
                seqs[i] = num;
            }
        }
        return seqs.size();
    }

    int bisect_left(vector<int>& nums, int tgt) {
        int l = 0;
        int r = nums.size();
        while (l < r) {
            int mid = (l + r) / 2;
            if (nums[mid] < tgt) 
                l = mid + 1;
            else
                r = mid;
        }
        return l;
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
