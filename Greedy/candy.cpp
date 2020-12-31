#include <iostream>
#include <vector>
// #include <unordered_set>
// #include <unordered_map>
#include <stack>
#include <string>
// #include <tuple> 
// #include <queue>
// #include <functional>
#include <algorithm>

using std::stack;
using std::vector;
// using std::priority_queue;
// using std::greater; // functional
// using std::unordered_set;
// using std::unordered_map;
using std::pair;
using std::string;
// using std::tuple;


// minHeap: priority_queue <int,vector<int>,greater<int>> q; 
// maxHeap: priority_queue <int,vector<int>,less<int> >q;

class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();
        vector<int> left(n, 1);
        for (int i = 1; i < n; i++) {
            if (ratings[i] > ratings[i-1])
                left[i] = left[i-1] + 1;
        }
        int ans = left[n-1];
        for (int i = n-2; i >= 0; i--) {
            if (ratings[i] > ratings[i+1]) {
                left[i] = std::max(left[i], left[i+1] + 1);
            }
            ans += left[i];
        }
        return ans;
    }
};


int main () 
{
    vector<int> ratings {1,3,4,5,2};
    Solution sol;
    int ans = sol.candy(ratings);
    std::cout << ans << '\n';
    return 0;
}