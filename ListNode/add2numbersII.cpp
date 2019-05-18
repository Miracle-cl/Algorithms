#include <iostream>
#include <vector>
#include <stack>

using std::vector;
using std::stack;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* create_list(const vector<int>& arr) {
        ListNode dummy(0);
        ListNode* p = &dummy;
        for (auto x : arr) {
            p->next = new ListNode(x);
            p = p->next;
        }
        return dummy.next;
    }

    ListNode* addTwoNumbers(ListNode* m, ListNode* n) {
        ListNode dummy(0);
        ListNode* p = &dummy;
        int cn = 0;
        while (m || n) {
            int val = cn + (m ? m->val : 0) + (n ? n->val : 0);
            cn = val / 10;
            p->next = new ListNode(val % 10);
            p = p->next;
            if (m)
                m = m->next;
            if (n)
                n = n->next;
        }
        return dummy.next;
    }

    ListNode* addTwoNumbersII(ListNode* m, ListNode* n) {
        stack<int> s1;
        stack<int> s2;
        stack<int> res;
        while (m) {
            s1.push(m->val);
            m = m->next;
        }

        while (n) {
            s2.push(n->val);
            n = n->next;
        }

        int cn = 0;
        while (!s1.empty() || !s2.empty()) {
            int val = cn + (s1.empty() ? 0 : s1.top()) + (s2.empty() ? 0 : s2.top());
            cn = val / 10;
            res.push(val % 10);
            if (!s1.empty())
                s1.pop();
            if (!s2.empty())
                s2.pop();
        }

        ListNode dummy(0);
        ListNode* p = &dummy;
        while (!res.empty()) {
            p->next = new ListNode(res.top());
            p = p->next;
            res.pop();
        }
        return dummy.next;
    }
};


int main()
{
    vector<int> a1 {7, 2, 6, 4};
    vector<int> a2 {5, 4, 3};
    Solution solu;
    ListNode* l1 = solu.create_list(a1);
    ListNode* l2 = solu.create_list(a2);
    ListNode* q = solu.addTwoNumbersII(l1, l2);
    while (q) {
        std::cout << q->val << " ";
        q = q->next;
    }
    return 0;
}
