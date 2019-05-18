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
    ListNode* create_list(const vector<int>& arr) {
        ListNode dummy(0);
        ListNode* p = &dummy;
        for (auto x : arr) {
            p->next = new ListNode(x);
            p = p->next;
        }
        return dummy.next;
    }

    ListNode* partition_list(ListNode* head, int x) {
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode* prev = dummy;
        ListNode* cur = head;
        while (prev->next && prev->next->val < x) {
            prev = prev->next;
        }
        cur = prev->next;
        while (cur->next) {
            if (cur->next->val < x) {
                ListNode* temp = cur->next;
                cur->next = temp->next;
                temp->next = prev->next;
                prev->next = temp;
                prev = prev->next;
                // ListNode* temp = prev->next;
                // prev->next = cur->next;
                // cur->next = cur->next->next;
                // prev = prev->next;
                // prev->next = temp;
            }
            else {
                cur = cur->next;
            }
        }
        return dummy->next;
    }
};


int main()
{
    std::vector<int> v {1,4,3,2,5,2};
    Solution solu;
    ListNode* head = solu.create_list(v);
    ListNode* q = solu.partition_list(head, 3);
    while (q) {
        std::cout << q->val << " ";
        q = q->next;
    }
    return 0;
}
