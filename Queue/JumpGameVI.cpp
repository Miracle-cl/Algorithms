#include <iostream>
#include <vector>
// #include <unordered_set>
// #include <unordered_map>
#include <stack>
#include <string>
// #include <tuple> 
#include <queue>
#include <deque>
// #include <functional>
#include <algorithm>

using std::stack;
using std::vector;
using std::priority_queue;
using std::deque;
using std::greater; // functional
// using std::unordered_set;
// using std::unordered_map;
using std::pair;
using std::make_pair;
using std::string;
// using std::tuple;


// minHeap: priority_queue <int,vector<int>,greater<int>> q; 
// maxHeap: priority_queue <int,vector<int>,less<int> >q;

class Solution {
public:
    int maxResult_0(vector<int>& nums, int k) {
        // priority_queue : nlogn
        priority_queue<pair<int, int>> pq;
        pq.emplace(make_pair(nums[0], 0));
        int n = nums.size();
        int ans = nums[0];
        for (int i = 1; i < n; i++) {
            while (!pq.empty() && i - pq.top().second > k)
                pq.pop();
            ans = pq.top().first + nums[i];
            pq.emplace(make_pair(ans, i));
        }
        return ans;
    }

    int maxResult(vector<int>& nums, int k) {
        // monotonic queue : n
        deque<pair<int, int>> pq;
        pq.emplace_back(make_pair(nums[0], 0));
        int n = nums.size();
        int ans = nums[0];
        for (int i = 1; i < n; i++) {
            // i is out of window k
            while (!pq.empty() && i - pq.front().second > k)
                pq.pop_front();
            ans = pq.front().first + nums[i];
            // not monotonic
            while (!pq.empty() && ans >= pq.back().first)
                pq.pop_back();
            pq.emplace_back(make_pair(ans, i));
        }
        return ans;
    }
};

int main () 
{
    vector<int> nums {10,-5,-2,4,0,3};
    int k = 3;
    Solution sol;
    int ans = sol.maxResult(nums, k);
    std::cout << ans << '\n';
    return 0;
}