/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if (!head || !head->next)
            return head;
        ListNode* first = new ListNode(-1);
        ListNode* second = new ListNode(-1);
        ListNode *p = head, *odd = first, *even = second;
        int idx = 1;
        while (p) {
            if (idx % 2 == 1) {
                odd->next = p;
                odd = odd->next;
            }
            else {
                even->next = p;
                even = even->next;
            }
            p = p->next;
            idx++;
        }
        odd->next = second->next;
        even->next = NULL;
        return first->next;
    }

    ListNode* oddEvenList2(ListNode* head) {
        if (!head || !head->next)
            return head;
        ListNode* odd = head;
        ListNode* evenbegin = head->next;
        ListNode* even = evenbegin;
        while (even->next && even->next->next) {
            odd->next = even->next;
            even->next = even->next->next;
            odd = odd->next;
            even = even->next;
        }
        if (even->next) {
            odd->next = even->next;
            odd = odd->next;
        }
        odd->next = evenbegin;
        even->next = NULL;
        return head;
    }
};
