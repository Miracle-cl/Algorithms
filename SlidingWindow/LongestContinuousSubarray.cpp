#include <iostream>
#include <vector>
#include <deque>
#include <set>


using std::multiset;
using std::vector;
using std::deque;



class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        deque<int> maxq, minq;
        int lens = 0;
        for (int l = 0, r = 0; r < nums.size(); ++r) {
            while (!minq.empty() && minq.back() > nums[r])
                minq.pop_back();
            while (!maxq.empty() && maxq.back() < nums[r])
                maxq.pop_back();
            minq.emplace_back(nums[r]);
            maxq.emplace_back(nums[r]);

            if (maxq.front() - minq.front() <= limit) {
                lens = std::max(lens, r - l + 1);
            }
            else {
                if (maxq.front() == nums[l]) 
                    maxq.pop_front();
                else if (minq.front() == nums[l])
                    minq.pop_front();
                ++l;
            }
        }
        return lens;
    }
    int longestSubarray_1(vector<int>& nums, int limit) {
        multiset<int> s;
        int lens = 0;
        for (int l = 0, r = 0; r < nums.size(); ++r) {
            s.insert(nums[r]);
            if (*s.crbegin() - *s.cbegin() <= limit) {
                lens = std::max(lens, r - l + 1);
            }
            else {
                s.erase(s.find(nums[l++]));
                // auto it = s.find(nums[l++]);
                // s.erase(it);
                // ++l;
            }
        }
        return lens;
    }
};



int main ()
{
    Solution sol;
    int limit = 2;
    vector<int> nums {2,2,2,4,4,2,5,5,5,5,5,2};
    int res = sol.longestSubarray(nums, limit);
    std::cout << res << '\n';
    return 0;
}