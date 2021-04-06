#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <unordered_map>

using std::vector;
using std::priority_queue;
using std::unordered_map;

class Solution {
private:
    struct Event {
        int loc;
        int height;
        int type;

        Event(int a, int b, int c) : loc(a), height(b), type(c) {}

        bool operator<(const Event& e) {
            // if entering, first process highest
            // if leaving, first process shortest
            if (loc == e.loc)
                return height * type > e.height * e.type;
            return loc < e.loc;
        }
    };
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        vector<Event> events;
        priority_queue<int> pq;
        vector<vector<int>> res;
        unordered_map<int, int> mp;

        for (auto& building : buildings) {
            events.push_back(Event(building[0], building[2], 1));
            events.push_back(Event(building[1], building[2], -1));
        }
        std::sort(events.begin(), events.end());

        for (auto& e: events) {
            if (e.type == 1) {
                // entering
                if (pq.empty() || pq.top() < e.height) 
                    res.push_back({e.loc, e.height});
                pq.push(e.height);
            }
            else {
                // leaving
                // remove val from pq
                mp[e.height]++;
                while (!pq.empty() && mp[pq.top()] > 0) {
                    mp[pq.top()]--;
                    pq.pop();
                }
                if (pq.empty())
                    res.push_back({e.loc, 0});
                else if (e.height > pq.top())
                    res.push_back({e.loc, pq.top()});
            }
        }

        return res;
    }
};

int main()
{
    Solution sol;
    // vector<vector<int>> buildings {{0,2,3},{0,2,4}};
    // vector<vector<int>> buildings {{0,2,3},{2,5,4}};
    // vector<vector<int>> buildings {{0,2,3},{2,5,3}};
    vector<vector<int>> buildings {{2,9,10},{3,7,15},{5,12,12},{15,20,10},{19,24,8}};
    vector<vector<int>> res = sol.getSkyline(buildings);

    for (auto& e: res) {
            std::cout << e[0] << ' ' << e[1] << '\n';
        }

    return 0;
}