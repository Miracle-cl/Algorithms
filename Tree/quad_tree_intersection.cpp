#include <iostream>

/*
A:                 B:                 C (A or B):
+-------+-------+  +-------+---+---+  +-------+-------+
|       |       |  |       | F | F |  |       |       |
|   T   |   T   |  |   T   +---+---+  |   T   |   T   |
|       |       |  |       | T | T |  |       |       |
+-------+-------+  +-------+---+---+  +-------+-------+
|       |       |  |       |       |  |       |       |
|   F   |   F   |  |   T   |   F   |  |   T   |   F   |
|       |       |  |       |       |  |       |       |
+-------+-------+  +-------+-------+  +-------+-------+
*/

// Definition for a QuadTree node.
class Node {
public:
    bool val;
    bool isLeaf;
    Node* topLeft;
    Node* topRight;
    Node* bottomLeft;
    Node* bottomRight;

    Node() {}

    Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node* _bottomLeft, Node* _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
};

class Solution {
public:
    Node* intersect(Node* quadTree1, Node* quadTree2) {
        if (quadTree1->isLeaf)
            return (quadTree1->val) ? quadTree1 : quadTree2;
        else if (quadTree2->isLeaf)
            return (quadTree2->val) ? quadTree2 : quadTree1;
        else {
            Node* tl = intersect(quadTree1->topLeft, quadTree2->topLeft);
            Node* tr = intersect(quadTree1->topRight, quadTree2->topRight);
            Node* bl = intersect(quadTree1->bottomLeft, quadTree2->bottomLeft);
            Node* br = intersect(quadTree1->bottomRight, quadTree2->bottomRight);

            // Node* result_node = new Node

            if (tl->isLeaf && tr->isLeaf && bl->isLeaf && br->isLeaf && tl->val == tr->val && tl->val == bl->val && tl->val == br->val)
                return new Node(tl->val, true, nullptr, nullptr, nullptr, nullptr);
            else
                return new Node(false, false, tl, tr, bl, br);
        }
    }
};

int main()
{
    // define quadTree1
    Node* q1_tl = new Node(true, true, nullptr, nullptr, nullptr, nullptr);
    Node* q1_tr = new Node(true, true, nullptr, nullptr, nullptr, nullptr);
    Node* q1_bl = new Node(false, true, nullptr, nullptr, nullptr, nullptr);
    Node* q1_br = new Node(false, true, nullptr, nullptr, nullptr, nullptr);
    Node* q1 = new Node(true, false, q1_tl, q1_tr, q1_bl, q1_br);

    return 0;
}
