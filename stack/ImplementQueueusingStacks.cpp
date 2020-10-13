#include <iostream>
// #include <vector>
#include <stack>
// #include <queue>

using std::stack;


class MyQueue {
    stack<int> s1;
    stack<int> s2;
public:
    /** Initialize your data structure here. */
    MyQueue() {
        
    }
    
    /** Push element x to the back of queue. */
    void push(int x) {
        s1.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        if (this->empty())
            return -1;
        if (s2.empty()) {
            while (!s1.empty()) {
                s2.push(s1.top());
                s1.pop();
            }
        }
        int front = s2.top();
        s2.pop();
        return front;
    }
    
    /** Get the front element. */
    int peek() {
        int front = this->pop();
        s2.push(front);
        return front;
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        return s1.empty() && s2.empty();
    }
};


int main()
{
    MyQueue* obj = new MyQueue();
    obj->push(1);
    obj->push(2);
    int param_2 = obj->pop();
    std::cout << param_2 << '\n';
    int param_3 = obj->peek();
    std::cout << param_3 << '\n';
    bool param_4 = obj->empty();
    std::cout << param_4 << '\n';
    return 0;
}