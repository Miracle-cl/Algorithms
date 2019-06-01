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
    ListNode * create_linked_list(const vector<int>& nums) {
        ListNode dummy(-1);
        ListNode* p = &dummy;
        for (auto n : nums) {
            p->next = new ListNode(n);
            p = p->next;
        }
        return dummy.next;
    }

    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (!headA || !headB)
            return NULL;
        int lenA = length(headA), lenB = length(headB);
        if (lenA > lenB) {
            for (int i = 0; i < lenA-lenB; i++)
                headA = headA->next;
        }
        else {
            for (int i = 0; i < lenB-lenA; i++)
                headB = headB->next;
        }
        std::cout << headA->val << headB->val << "\n";
        while (headA && headB && headA != headB) {
            headA = headA->next;
            headB = headB->next;
        }
        std::cout << (headA == NULL) << "\n";
        return (headA && headB) ? headA : NULL;
    }

    int length(ListNode *head) {
        int len = 0;
        while (head) {
            len++;
            head = head->next;
        }
        return len;
    }

    ListNode *getIntersectionNode2(ListNode *headA, ListNode *headB) {
        if (!headA || !headB)
            return NULL;
        ListNode* pa = headA;
        ListNode* pb = headB;

        while (pa != pb) {
            pa = pa ? pa->next : headB;
            pb = pb ? pb->next : headA;
        }
        return pa;
    }
};


int main()
{
    std::vector<int> v1 {4,1,8,4,5};
    std::vector<int> v2 {5,0,1,8,4,5};
    // test case is wrong
    Solution s;
    ListNode* a = s.create_linked_list(v1);
    ListNode* b = s.create_linked_list(v2);
    ListNode* p = s.getIntersectionNode(a, b);
    if (p)
        std::cout << p->val << "\n";
    else
        std::cout << "NULL\n";
    return 0;
}
