#include <iostream>
#include <string>

using std::string;

class Solution {
public:
    string convertToTitle(int n) {
        string res = "";
        // char c;
        while (n > 0) {
            char c = (n-1) % 26 + 'A';
            res = c + res;
            n = (n-1) / 26;
        }
        return res;
    }
};

int main()
{
    Solution s;
    int arr[5] = {1, 27, 28, 701, 1000};
    // std::cout << s.convertToTitle(1) << "\n";
    for (int n : arr)
        std::cout << s.convertToTitle(n) << "\n";
    return 0;
}
