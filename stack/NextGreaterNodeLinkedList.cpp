#include <iostream>
#include <vector>
#include <stack>

using std::vector;
using std::stack;
// monotonic stack

// Definition for singly-linked list.
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

    vector<int> nextLargerNodes(ListNode* head) {
        vector<int> nums;
        if (!head)
            return nums;
        while (head) {
            nums.push_back(head->val);
            head = head->next;
        }
        stack<int> stk; // monotonic stack
        int temp;
        for (int i = nums.size()-1; i >= 0; i--) {
            temp = nums[i];
            while (!stk.empty() and stk.top() <= temp)
                stk.pop();
            nums[i] = stk.empty() ? 0 : stk.top();
            stk.push(temp);
        }
        return nums;
    }
};

int main()
{
    vector<int> nums {4,3,2,5,1,8,10};
    Solution s;
    ListNode* head = s.create_list(nums);
    vector<int> res = s.nextLargerNodes(head);
    for (auto n: res) {
        std::cout << n << " ";
    }
    std::cout << "\n";
    return 0;
}
