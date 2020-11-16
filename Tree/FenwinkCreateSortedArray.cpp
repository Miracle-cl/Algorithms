#include <iostream>
#include <vector>
#include <algorithm>


using std::vector;


class FenwickTree {
private:
    int n;
    vector<int> sums;
public:
    // int n;
    // vector<int> sums;
    FenwickTree(int n): n(n), sums(vector<int>(n+1, 0)) {}

    void update(int i, int val) {
        while (i <= n) {
            sums[i] += val;
            i += i & -i;
        }
    }

    int query(int i) {
        int ans = 0;
        while (i > 0) {
            ans += sums[i];
            i -= i & -i;
        }
        return ans;
    }

    // void print() {
    //     for (int x : sums)
    //         std::cout << x << ' ';
    //     std::cout << '\n';
    // }
};


class Solution {
public:
    int createSortedArray(vector<int>& instructions) {
        constexpr int mode = 1000000007; 
        int n = *std::max_element(instructions.begin(), instructions.end());
        FenwickTree ft(n);
        long long cost = 0;
        for (int i = 0; i < instructions.size(); i++) {
            ft.update(instructions[i], 1);
            int smaller = ft.query(instructions[i]-1);
            int larger = i + 1 - ft.query(instructions[i]);
            cost += std::min(smaller, larger);
        }
        return cost % mode;
    }
};

int main () 
{
    vector<int> instructions {1,3,3,3,2,4,2,1,2};
    Solution solu;
    int res = solu.createSortedArray(instructions);
    std::cout << res << '\n';
    return 0;
}
