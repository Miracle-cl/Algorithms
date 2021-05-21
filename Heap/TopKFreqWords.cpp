#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <unordered_map>
#include <algorithm>


using std::string;
using std::vector;
using std::pair;
using std::priority_queue;
using std::unordered_map;


// priority_queue with pair<string, int>
// priority_queue<pair<string, int>, vector<pair<string, int>>, decltype(cmp)> pq(cmp);


class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> cnt;
        for (string& w : words) {
            cnt[w]++;
        }
        vector<string> res;
        for (auto& x: cnt) {
            res.emplace_back(x.first);
        }
        std::sort(res.begin(), res.end(), [&](const string& a, const string& b) -> bool {
            return (cnt[a] > cnt[b]) || (cnt[a] == cnt[b] && a < b);
        });
        res.erase(res.begin() + k, res.end());
        return res;
    }

    vector<string> topKFrequent_1(vector<string>& words, int k) {
        unordered_map<string, int> cnt;
        for (string& w : words) {
            cnt[w]++;
        }
        auto cmp = [](const pair<string, int>& a, const pair<string, int>& b) {
            return a.second == b.second ? a.first < b.first : a.second > b.second;
        };
        priority_queue<pair<string, int>, vector<pair<string, int>>, decltype(cmp)> pq(cmp);
        for (auto& it : cnt) {
            pq.push(it);
            if (pq.size() > k) pq.pop();
        }
        vector<string> res(k);
        for (int i = k-1; i >= 0; --i) {
            res[i] = pq.top().first;
            pq.pop();
        }
        return res;
    }
};


int main () 
{
    vector<string> words {"i", "love", "leetcode", "i", "love", "coding", "love"};
    int k = 2;
    Solution sol;
    vector<string> res = sol.topKFrequent_1(words, k);

    std::cout << res[0] << '\n';
    return 0;
}

