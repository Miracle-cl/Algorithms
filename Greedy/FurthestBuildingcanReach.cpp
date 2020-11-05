#include <iostream>
#include <vector>
#include <queue>
#include <functional>

using std::vector;
using std::priority_queue;
using std::greater; // functional


// minHeap: priority_queue <int,vector<int>,greater<int>> q; 
// maxHeap: priority_queue <int,vector<int>,less<int> >q;

class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        int n = heights.size();
        int use_brick = 0;
        priority_queue<int, vector<int>, greater<int>> q;
        for (int i = 1; i < n; i++) {
            int dh = heights[i] - heights[i-1];
            if (dh <= 0)
                continue;
            q.emplace(dh);
            if (q.size() > ladders) {
                use_brick += q.top();
                q.pop();
            }
            if (use_brick > bricks)
                return i - 1;
        }
        return n - 1;
    }
};


int main () 
{
    vector<int> heights{4,12,2,7,3,18,20,3,19};
    Solution solu;
    int res = solu.furthestBuilding(heights, 10, 2);
    std::cout << res << '\n';
    return 0;
}
