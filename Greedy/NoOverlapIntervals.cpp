#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;

class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if (intervals.empty()) return 0;
        int ans = 0;
        std::sort(intervals.begin(), intervals.end());
        int pt = intervals[0][1];
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i][0] >= pt)
                pt = intervals[i][1];
            else {
                ans++;
                pt = std::min(pt, intervals[i][1]);
            }
        }
        return ans;
    }
};


int main()
{
    vector<vector<int>> intervals {{1,2}, {1,2}};
    Solution sol;
    int res = sol.eraseOverlapIntervals(intervals);
    std::cout << res << '\n';
    return 0;
}