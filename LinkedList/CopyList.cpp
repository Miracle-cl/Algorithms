#include <iostream>
#include <unordered_map>

using std::unordered_map;

class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node() {}

    Node(int _val, Node* _next, Node* _random) {
        int val = _val;
        Node* next = _next;
        Node* random = _random;
    }
};

class S {
public:
    Node* copyRandomList(Node* head) {
        Node dummy(-1, head, NULL);
        return dummy.next;
    }
};

int main()
{
    unordered_map<Node*, Node*> mymap;
    Node dummy(5, NULL, NULL);
    Node* p = &dummy;

    for (int i = 1; i < 5; i++) {
        p->next = new Node;
        p->next->val = i;
        p->next->next = NULL;
        p->next->random = NULL;
        p = p->next;
    }
    Node* q = dummy.next;
    while (q) {
        std::cout << q->val << "\n";
        q = q->next;
    }

    // mymap[p] = new Node(p->val, NULL, NULL);

    return 0;
}
