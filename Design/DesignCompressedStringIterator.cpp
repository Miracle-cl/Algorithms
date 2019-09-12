#include <iostream>
#include <string>

using std::string;

// StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");
//
// iterator.next(); // return 'L'
// iterator.next(); // return 'e'
// iterator.next(); // return 'e'
// iterator.next(); // return 't'
// iterator.next(); // return 'C'
// iterator.next(); // return 'o'
// iterator.next(); // return 'd'
// iterator.hasNext(); // return true
// iterator.next(); // return 'e'
// iterator.hasNext(); // return false
// iterator.next(); // return ' '

class StringIterator {
public:
    StringIterator(string compressedString) {
        s = compressedString;
        n = s.size();
        i = 0;
        cnt = 0;
    }

    char next() {
        if (hasNext()) {
            cnt--;
            return c;
        }
        return '#'; // ' '
    }

    bool hasNext() {
        if (cnt > 0) return true;
        if (i >= n) return false;
        c = s[i++];
        while (i < n && s[i] >= '0' && s[i] <= '9')
            cnt = cnt * 10 + s[i++] - '0';
        return true;
    }

private:
    string s;
    int n, i, cnt;
    char c;
};


int main()
{
    StringIterator iterator = StringIterator("L1e2t1C1o1d1e1");
    for (int i = 0; i < 7; i++) {
        std::cout << iterator.next() << "\n";
    }
    std::cout << iterator.hasNext() << "\n";
    std::cout << iterator.next() << "\n";
    std::cout << iterator.hasNext() << "\n";
    std::cout << iterator.next() << "\n";
    return 0;
}
