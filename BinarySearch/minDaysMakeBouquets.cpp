#include <iostream>
#include <vector>


using std::vector;


class Solution {
public:
    int minDays(vector<int>& bloomDay, int m, int k) {
        int len = bloomDay.size();
        if (len < m * k) return -1;
        if (len == m * k) return *max_element(bloomDay.begin(), bloomDay.end());
        int l = *min_element(bloomDay.begin(), bloomDay.end());
        int r = *max_element(bloomDay.begin(), bloomDay.end());
        while (l < r) {
            int mid = (l + r) / 2;
            if (check(bloomDay, m, k, mid)) {
                r = mid;
            }
            else {
                l = mid + 1;
            }
        }
        return l;
    }

    bool check(vector<int>& bloomDay, int m, int k, int limit) {
        int day = 0, flowers = 0;
        for (int x : bloomDay) {
            if (x <= limit) {
                if (++day == k) {
                    flowers++;
                    day = 0;
                }
            }
            else {
                day = 0;
            }
            if (m <= flowers) return true;
        }
        return false;
    }

    bool check_1(vector<int>& bloomDay, int m, int k, int len, int limit) {
        for (int i = 0, j = 0; j < len; ++j) {
            if (bloomDay[j] > limit) {
                m -= (j - i) / k;
                i = j + 1;
            }
            else if (j == len - 1) {
                m -= (j - i + 1) / k;
            }
        }
        return m <= 0;
    }
};


int main () 
{
    vector<int>bloomDay {7,7,7,7,12,7,7};
    int m = 2, k = 3;
    
    Solution sol;
    int res = sol.minDays(bloomDay, m, k);

    // bool res = sol.check_1(bloomDay, m, k, 6, 16);
    std::cout << res << '\n';
    return 0;
}