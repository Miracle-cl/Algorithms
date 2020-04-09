#include <iostream>
#include <vector>

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* create_list(const std::vector<int>& v) {
        ListNode dummy(-1);
        ListNode* p = &dummy;
        for (auto n : v) {
            p->next = new ListNode(n);
            p = p->next;
        }
        return dummy.next;
    }

    ListNode* deleteDuplicates(ListNode* head) {
        ListNode dummy(-1);
        ListNode* prev = &dummy;
        prev->next = head;
        while (prev->next) {
            ListNode* cur = prev->next;
            while (cur->next && cur->val == cur->next->val)
                cur = cur->next;
            if (cur != prev->next)
                prev->next = cur->next;
            else
                prev = prev->next;
        }
        return dummy.next;
    }
};

int main()
{
    std::vector<int> v {1,2,2,3,4,4,5,5,5,6};
    Solution s;
    ListNode* head = s.create_list(v);
    // std::cout << head->val << "\n";
    ListNode* q = s.deleteDuplicates(head);
    while (q) {
        std::cout << q->val << "\n";
        q = q->next;
    }
    return 0;
}
