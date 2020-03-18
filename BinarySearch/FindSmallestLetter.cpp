#include <iostream>
#include <vector>

using std::vector;

class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        int l = 0, r = letters.size();
        while (l < r) {
            int mid = (l + r) / 2;
            if (letters[mid] <= target)
                l = mid + 1;
            else
                r = mid;
        }
        return r < letters.size() ? letters[r] : letters[0];
    }
};

int main()
{
    Solution s;
    char target = 'a';
    vector<char> letters {'c', 'f', 'j'};
    char c = s.nextGreatestLetter(letters, target);
    std::cout << c << "\n";
    return 0;
}
