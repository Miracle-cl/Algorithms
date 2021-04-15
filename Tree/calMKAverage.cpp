#include <iostream>
#include <queue>
#include <set>


using std::queue;
using std::multiset;



class MKAverage {
private:
    int m, k, n;
    long sum;
    multiset<int> left, mid, right;
    queue<int> q;

    void add(int val) {
        left.insert(val);

        if (left.size() > k) {
            auto it = prev(left.end());
            sum += *it;
            mid.insert(*it);
            left.erase(it);
        }

        if (mid.size() > n) {
            auto it = prev(mid.end());
            sum -= *it; 
            right.insert(*it);
            mid.erase(it);
        }
    }

    void remove(int val) {
        if (val <= *left.rbegin()) {
            left.erase(left.find(val));
        }
        else if (val <= *mid.rbegin()) {
            mid.erase(mid.find(val));
            sum -= val;
        }
        else {
            right.erase(right.find(val));
        }

        if (left.size() < k) {
            auto it = mid.begin();
            sum -= *it;
            left.insert(*it);
            mid.erase(it);
        }

        if (mid.size() < n) {
            auto it = right.begin();
            sum += *it;
            mid.insert(*it);
            right.erase(it);
        }
    }
public:
    MKAverage(int m, int k) : sum(0), m(m), k(k), n(m-2*k) {

    }
    
    void addElement(int num) {
        if (q.size() == m) {
            remove(q.front());
            q.pop();
        }
        add(num);
        q.push(num);
    }
    
    int calculateMKAverage() {
        return (q.size() < m) ? -1 : sum / n;
    }
};




int main()
{
    MKAverage mka(3, 1);
    mka.addElement(586);
    mka.addElement(899);
    int r1 = mka.calculateMKAverage();
    mka.addElement(546);
    mka.addElement(23);
    int r2 = mka.calculateMKAverage();
    // mka.addElement(586);
    // mka.addElement(586);
    // mka.addElement(586);
    std::cout << r1 << std::endl;
    std::cout << r2 << std::endl;
    return 0;
}

