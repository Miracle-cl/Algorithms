#include <iostream>
#include <vector>

using std::vector;

class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        int n = nums.size();
        if (n < 2)
            return n;

        vector<int> length(n, 0);
        vector<int> cnt(n, 1);
        int longest = 0;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    if (length[j] >= length[i]) {
                        length[i] = length[j] + 1;
                        cnt[i] = cnt[j];
                    }
                    else if (length[j] + 1 == length[i]) {
                        cnt[i] += cnt[j];
                    }
                }
            }
            if (longest < length[i])
                longest = length[i];
        }
        int res = 0;
        for (int k = 0; k < n; k++) {
            if (length[k] == longest) res += cnt[k];
        }
        return res;
    }

    int findNumberOfLIS1(vector<int>& nums) {
        int N = nums.size();
        if (N < 2)
            return N;
        int *lengths, *counts;
        int longest = 0, res = 0;
        // lengths = new int[N] (); // init = 0
        lengths = new int[N]; // without initial
        counts = new int[N];
        for (int i = 0; i < N; i++) {
            lengths[i] = 1;
            counts[i] = 1;
        }
        for (int i = 1; i < N; i++) {
            for (int j = 0; j < i; j++) {
                // j i
                if (nums[i] > nums[j]) {
                    if (lengths[j] >= lengths[i]) {
                        lengths[i] = lengths[j] + 1;
                        counts[i] = counts[j];
                    }
                    else if (lengths[j] + 1 == lengths[i])
                        counts[i] += counts[j];
                }
                if (lengths[i] > longest) longest = lengths[i];
            }
        }
        for (int i = 0; i < N; i++) {
            // std::cout << lengths[i] << ' ';
            // std::cout << counts[i] << '\n';
            if (lengths[i] == longest) res += counts[i];
        }
        delete [] lengths;
        delete [] counts;
        return res;
    }
};

int main()
{
    Solution solu;
    vector<int> v {1,3,5,4,7,7};
    int res = solu.findNumberOfLIS(v);
    std::cout << res << "\n";
    return 0;
}
