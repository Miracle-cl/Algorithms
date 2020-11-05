#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>


using std::vector;
using std::unordered_set;
using std::unordered_map;


class RandomizedCollection {
    vector<int> nums;
    unordered_map<int, unordered_set<int>> pos;
public:
    /** Initialize your data structure here. */
    RandomizedCollection() {
        
    }
    
    /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
    bool insert(int val) {
        int i = nums.size();
        nums.emplace_back(val);
        if (pos.count(val) == 0) {
            pos[val] = {i};
            return true;
        }
        else {
            pos[val].emplace(i);
            return false;
        }
    }
    
    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
    bool remove(int val) {
        if (pos.find(val) != pos.end()) {
            int r = nums.size() - 1;
            int i = *pos[val].begin();
            if (i == r) {
                pos[val].erase(i);
                nums.pop_back();
            }
            else {
                pos[val].erase(i);
                nums[i] = nums[r];
                pos[nums[r]].emplace(i);
                pos[nums[r]].erase(r);
                nums.pop_back();
            }
            if (pos[val].empty())
                pos.erase(val);
            return true;
        }
        return false;
    }
    
    /** Get a random element from the collection. */
    int getRandom() {
        return nums[rand() % nums.size()];
    }

    void show_pos() {
        for (int n : nums) 
            std::cout << n << ' ';
        std::cout << '\n';
        for (auto& x : pos) {
            std::cout << x.first << ": ";
            for (auto it = x.second.begin(); it != x.second.end(); it++) {
                std::cout << *it << ' ';
            }
            std::cout << '\n';
        }
    }
};



int main () {
    vector<int> ins{1,1,2,1,2,2};
    vector<int> rms{1,2,2,2};
    RandomizedCollection rc;
    std::cout << "insert\n";
    for (int i : ins) {
        std::cout << i << ':' << rc.insert(i) << '\n';
    }
    rc.show_pos();
    std::cout << "remove\n";
    for (int r : rms) {
        std::cout << r << ':' << rc.remove(r) << '\n';
        
    }
    rc.show_pos();
    std::cout << "getRand\n";
    std::cout << rc.getRandom() << '\n';
    return 0;
}