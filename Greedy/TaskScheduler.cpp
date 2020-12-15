#include <iostream>
#include <vector>
#include <algorithm>


using std::vector;


class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> freqs(26, 0);
        for (const char& t : tasks) 
            freqs[t - 'A']++;
        int max_cnt = *std::max_element(freqs.begin(), freqs.end());
        // int ans = (max_cnt - 1) * (n + 1); 
        // int ans, size_t tasks.size() cannot compare - max
        size_t ans = (max_cnt - 1) * (n + 1);
        // for (int f : freqs) {
        //     if (f == max_cnt) 
        //         ans++;
        // }
        ans += std::count_if(freqs.begin(), freqs.end(), [&max_cnt](int c) {return c==max_cnt;});
        return std::max(tasks.size(), ans);
    }
};

int main()
{
    int n = 2;
    vector<char> tasks {'A','A','A','A','A','A','B','C','D','E','F','G'};

    Solution solu;
    int res = solu.leastInterval(tasks, n);
    std::cout << res << '\n';
    return 0;

}
