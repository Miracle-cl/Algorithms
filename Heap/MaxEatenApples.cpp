#include <iostream>
#include <vector>
// #include <unordered_set>
// #include <unordered_map>
#include <stack>
#include <string>
// #include <tuple> 
#include <queue>
// #include <functional>
#include <algorithm>

using std::stack;
using std::vector;
using std::priority_queue;
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
    #define pii pair<int, int>
    int eatenApples(vector<int>& apples, vector<int>& days) {
        int n = apples.size();
        int ans = 0;
        // store_days, apple_num
        priority_queue<pii, vector<pii>, greater<pii>> pq;
        for (int i = 0; i < n; i++) {
            if (apples[i] > 0)
                pq.emplace(make_pair(i+days[i], apples[i]));
            while (!pq.empty() && pq.top().first <= i)
                pq.pop();
            if (!pq.empty()) {
                ans++;
                int day = pq.top().first;
                int apple = pq.top().second;
                apple--;
                pq.pop();
                if (day > i && apple > 0)
                    pq.emplace(make_pair(day, apple));
            }
        }
        int i = n;
        while (!pq.empty()) {
            while (!pq.empty() && pq.top().first <= i)
                pq.pop();
            if (!pq.empty()) {
                ans++;
                int day = pq.top().first;
                int apple = pq.top().second;
                apple--;
                pq.pop();
                if (day > i && apple > 0)
                    pq.emplace(make_pair(day, apple));
            }
            i++;
        }
        return ans;
    }
};

int main () 
{
    vector<int> apples {1,2,3,5,2};
    vector<int> days {3,2,1,4,2};
    Solution sol;
    int ans = sol.eatenApples(apples, days);
    std::cout << ans << '\n';
    return 0;
}
