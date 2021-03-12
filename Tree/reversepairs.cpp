#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using std::vector;
using std::unordered_map;


class BIT {
private:
    int size;
    vector<int> sum;
public:
    BIT(int n) : size(n), sum(n+1) {}

    void update(int id, int val) {
        while (id <= size) {
            sum[id] += val;
            id += low_bit(id);
        }
    }

    int query(int id) {
        int ret = 0;
        while (id > 0) {
            ret += sum[id];
            id -= low_bit(id);
        }
        return ret;
    }

    static int low_bit(int x) {
        return x & (-x);
    }
};

class Solution {
public:
    int reversePairs(vector<int>& nums) {
        vector<int> tmp = nums;
        std::sort(tmp.begin(), tmp.end());
        unordered_map<int, int> mp;
        for (int t : tmp) {
            if (mp.count(t) > 0)
                continue;
            mp[t] = mp.size() + 1;
        }
        std::reverse(nums.begin(), nums.end());

        BIT bi_tree(mp.size());
        int ans = 0;
        for (int num : nums) {
            ans += bi_tree.query(mp[num]-1);
            bi_tree.update(mp[num], 1);
        }
        return ans;
    }
};


int main()
{
    vector<int> nums {7,5,6,4};
    Solution sol;
    int res = sol.reversePairs(nums);
    std::cout << res << '\n';
    return 0;
}