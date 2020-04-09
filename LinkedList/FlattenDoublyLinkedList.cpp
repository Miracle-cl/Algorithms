#include <iostream>
#include <vector>

using std::vector;

// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;

    Node() {}

    Node(int _val, Node* _prev, Node* _next, Node* _child) {
        val = _val;
        prev = _prev;
        next = _next;
        child = _child;
    }
};

class Solution {
public:
    Node* flatten(Node* head) {
        vector<int> res;
        preorder(head, res);
        Node* dummy = new Node(-1, NULL, NULL, NULL);
        Node* pre = dummy;
        Node* cur = NULL;
        for (int i = 0; i < res.size(); i++) {
            cur = new Node(res[i], NULL, NULL, NULL);
            pre->next = cur;
            if (i > 0)
                cur->prev = pre;
            pre = cur;
        }
        return dummy->next;
    }

    void preorder(Node* node, vector<int>& res) {
        if (!node)
            return;
        res.push_back(node->val);
        preorder(node->child, res);
        preorder(node->next, res);
    }

    Node* flatten2(Node* head) {
        Node* cur = head;
        while (cur) {
            if (cur->child) {
                Node* nxt = cur->next;
                Node* chd = cur->child;
                while (chd->next)
                    chd = chd->next;
                chd->next = nxt;
                cur->next = cur->child;
                cur->child->prev = cur;
                cur->child = NULL;
                if (nxt)
                    nxt->prev = chd;
            }
            cur = cur->next;
        }
        return head;
    }
};
