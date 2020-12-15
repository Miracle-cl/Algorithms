#include <iostream>
#include <list>
#include <queue>
#include <algorithm>
#include <iterator>


using std::list;
using std::queue;

class FrontMiddleBackQueue {
private:
    list<int> q;
    int lens;
public:
    FrontMiddleBackQueue(): q{std::initializer_list<int>{-1, -1}}, lens{2} {}
    
    void pushFront(int val) {
        q.insert(std::next(q.begin()), val);
        lens++;
    }
    
    void pushMiddle(int val) {
        auto it = q.begin();
        int mid = lens / 2;
        std::advance(it, mid);
        q.insert(it, val);
        lens++;
    }
    
    void pushBack(int val) {
        q.insert(std::prev(q.end()), val);
        lens++;
    }
    
    int popFront() {
        if (lens == 2)
            return -1;
        auto it = std::next(q.begin());
        int val = *it;
        q.erase(it);
        lens--;
        return val;
    }
    
    int popMiddle() {
        if (lens == 2)
            return -1;
        auto it = q.begin();
        int mid = (lens - 1) / 2;
        // std::cout << "xx " << mid << '\n';
        std::advance(it, mid);
        int val = *it;
        q.erase(it);
        lens--;
        return val;
    }
    
    int popBack() {
        if (lens == 2)
            return -1;
        auto it = std::prev(std::prev(q.end())); // double prev, std::prev(q.end()) is -1
        int val = *it;
        // std::cout << 'E' << val << '\n';
        // std::cout << 'E' << *it << '\n';
        q.erase(it);
        lens--;
        return val;
    }

    void show() {
        std::cout << "xx\n";
        for (std::list<int>::iterator it = q.begin(); it != q.end(); it++)
            std::cout << *it << ' ';
        std::cout << '\n' << lens << '\n';
    }
};


int main()
{
    FrontMiddleBackQueue fmbq;
    fmbq.pushFront(1);
    fmbq.pushBack(2);
    fmbq.pushMiddle(3);
    fmbq.pushMiddle(4);
    std::cout << fmbq.popFront() << '\n';
    std::cout << fmbq.popMiddle() << '\n';
    std::cout << fmbq.popMiddle() << '\n';
    // fmbq.show();
    std::cout << fmbq.popBack() << '\n';
    std::cout << fmbq.popFront() << '\n';
    fmbq.show();
    return 0;
}
