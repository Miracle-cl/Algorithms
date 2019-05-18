#include <iostream>
#include <vector>

using std::vector;

class Solution {
public:
    int majorityElement(const std::vector<int>& nums) {
        // if used hash table O(n), O(n);
        // this algorithms is 'Moore Voting' : O(n), O(1); space is less
        int res = nums[0];
        int count = 1;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] == res)
                count++;
            else {
                count--;
                if (count == 0) {
                    res = nums[i];
                    count++;
                }
            }
        }
        return res;
    }

    vector<int> majorityElementII(vector<int>& nums) {
        vector<int> res;
        int a = 0, b = 0, na = 0, nb = 0;
        for (auto num : nums) {
            if (a == num) {na++;}
            else if (b == num) {nb++;}
            else if (na == 0) {a = num; na++;}
            else if (nb == 0) {b = num; nb++;}
            else {na--; nb--;}
        }
        na = 0;
        nb = 0;
        for (auto num : nums) {
            if (num == a) {na++;}
            else if (num == b) {nb++;}
        }
        int flag = nums.size() / 3;
        if (na > flag)
            res.push_back(a);
        if (nb > flag)
            res.push_back(b);
        return res;
    }
};

int main()
{
    std::vector<int> v1 {2,3,3};
    std::vector<int> v2 {2,2,1,1,1,2,2};
    std::vector<int> v3 {1,1,1,3,3,2,2,2};
    Solution solu;
    // std::cout << solu.majorityElement(v1) << "\n";
    // std::cout << solu.majorityElement(v2) << "\n";
    vector<int> res = solu.majorityElementII(v3);
    for (auto n : res)
        std::cout << n << "\n";
    return 0;
}
