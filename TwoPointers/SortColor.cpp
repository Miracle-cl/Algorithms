#include <iostream>
#include <vector>

using std::vector;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int ptr = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) {
                std::swap(nums[ptr], nums[i]);
                ptr++;
            }
        }
        for (int i = ptr; i < nums.size(); i++) {
            if (nums[i] == 1) {
                std::swap(nums[ptr], nums[i]);
                ptr++;
            }
        } 
    }

    void sortColors_1(vector<int>& nums) {
        int p0 = 0, p2 = nums.size() - 1;
        for (int i = 0; i <= p2; i++) {
            while (nums[i] == 2 && i < p2) {
                std::swap(nums[i], nums[p2]);
                p2--;
            }
            if (nums[i] == 0) {
                std::swap(nums[p0], nums[i]);
                p0++;
            }
        }
    }
};


int main()
{
    int n = 2;
    // vector<int> v {2,0,2,1,1,0};
    vector<int> v {2,0,1};
    Solution solu;
    solu.sortColors_1(v);
    for (int x: v)
        std::cout << x << ' ';
    std::cout << '\n';
    return 0;
}