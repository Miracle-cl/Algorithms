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

    ListNode* rotate(ListNode* head, int k) {
        if (!head || !head->next)
            return head;
        int length = 0;
        ListNode* p = head;
        while (p->next) {
            p = p->next;
            length++;
        }
        p->next = head;
        k = k % (length + 1);
        // find prev of begin
        for (int i = 0; i < length - k; i++) {
            head = head->next;
        }
        ListNode* cur = head->next;
        head->next = NULL;
        return cur;
    }

};


int main()
{
    vector<int> a1 {1, 2, 3, 4, 5};
    int k = 5;
    Solution solu;
    ListNode* l1 = solu.create_list(a1);
    ListNode* q = solu.rotate(l1, k);
    int i = 0;
    while (q) {
        std::cout << q->val << " ";
        q = q->next;
        i++;
        if (i > 9) break;
    }
    return 0;
}
