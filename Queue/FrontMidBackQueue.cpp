#include <iostream>
#include <deque>

using std::deque;

class FrontMiddleBackQueue {
private:
    deque<int> front;
    deque<int> back;
    int lf = 0;
    int lb = 0;
public:
    FrontMiddleBackQueue() {}
    
    void pushFront(int val) {
        if (lf == 0 && lb == 0) {
            back.emplace_back(val);
            lb += 1;
            return;
        }
        if (lf == lb) {
            back.emplace_front(front.back());
            front.pop_back();
            lb++;
        }
        else
            lf++;
        
        front.emplace_front(val);
    }
    
    void pushMiddle(int val) {
        if (lf == lb) {
            back.emplace_front(val);
            lb++;
        }
        else {
            front.emplace_back(val);
            lf++;
        }
    }
    
    void pushBack(int val) {
        if (lf == lb)
            lb++;
        else {
            front.emplace_back(back.front());
            back.pop_front();
            lf++;
        }
        back.emplace_back(val);
    }
    
    int popFront() {
        if (lf == 0 && lb == 0)
            return -1;
        if (lf == 0) {
            int val = back.front();
            back.pop_front();
            lb--;
            return val;
        }
        if (lf == lb)
            lf--;
        else {
            front.emplace_back(back.front());
            back.pop_front();
            lb--;
        }
        int val = front.front();
        front.pop_front();
        return val;
    }
    
    int popMiddle() {
        if (lf == 0 && lb == 0)
            return -1;
        if (lf == lb) {
            int val = front.back();
            front.pop_back();
            lf--;
            return val;
        }
        int val = back.front();
        back.pop_front();
        lb--;
        return val;
    }
    
    int popBack() {
        if (lf == 0 && lb == 0)
            return -1;
        if (lf < lb)
            lb--;
        else {
            back.emplace_front(front.back());
            front.pop_back();
            lf--;
        }
        int val = back.back();
        back.pop_back();
        return val;
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
    std::cout << fmbq.popBack() << '\n';
    std::cout << fmbq.popFront() << '\n';
    return 0;
}