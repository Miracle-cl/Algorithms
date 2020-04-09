#include <iostream>
#include <vector>

using std::vector;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* create_list(const vector<int> & v) {
        ListNode dummy(-1);
        ListNode* p = &dummy;
        for (auto x : v) {
            p->next = new ListNode(x);
            p = p->next;
        }
        return dummy.next;
    }

    ListNode* swapPairs(ListNode* head) {
        ListNode dummy(-1);
        ListNode* prev = &dummy;
        prev->next = head;
        while (head && head->next) {
            prev->next = head->next;
            head->next = head->next->next;
            prev->next->next = head;
            prev = head;
            head = head->next;
        }
        return dummy.next;
    }

    ListNode* swapPairs1(ListNode* head) {
        // recursion
        if (!head || !head->next) return head;
        ListNode *t = head->next;
        head->next = swapPairs(head->next->next);
        t->next = head;
        return t;
    }
};

int main()
{
    std::vector<int> v {2, 3, 5, 6};
    Solution s;
    ListNode* p = s.create_list(v);
    ListNode* q = s.swapPairs(p);
    while (q) {
        std::cout << q->val << " ";
        q = q->next;
    }
    std::cout << "\n";
    return 0;
}
