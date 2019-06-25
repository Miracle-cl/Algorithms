#include <iostream>
#include <stdlib.h>

// using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int findTilt(TreeNode* root) {
        int tilt = 0;
        helper(root, &tilt);
        return tilt;
    }

    int helper(TreeNode* node, int* tilt) {
        if (node == NULL)
            return 0;
        int left_value = helper(node->left, tilt);
        int right_value = helper(node->right, tilt);
        (*tilt) += std::abs(left_value - right_value);
        return node->val + left_value + right_value;
    }

    TreeNode* test_tree() {
        TreeNode* root = new TreeNode(4);
        root->left = new TreeNode(2);
        root->right = new TreeNode(9);
        root->left->left = new TreeNode(3);
        root->left->right = new TreeNode(5);
        root->right->right = new TreeNode(7);
        return root;
    }
};

struct Node {
    int val;
    struct Node *left, *right;
};

class NodeSolution {
public:
    int traverse(Node *tree, int *tilt) {
        if (!tree)
            return 0;

        int left_sum = traverse(tree->left, tilt);
        int right_sum = traverse(tree->right, tilt);
        *tilt += std::abs(left_sum - right_sum);
        return left_sum + right_sum + tree->val;
    }

    int compute_tilt(Node *tree) {
        int tilt = 0;
        traverse(tree, &tilt);
        return tilt;
    }

    Node* new_node(int val) {
        Node* temp = new Node;
        temp->val = val;
        temp->left = temp->right = NULL;
        return temp;
    }

    Node* test_tree() {
        Node* root = NULL;
        root = new_node(4);
        root->left = new_node(2);
        root->right = new_node(9);
        root->left->left = new_node(3);
        root->left->right = new_node(5);
        root->right->right = new_node(7);
        return root;
    }
};


int main()
{
    NodeSolution ns;
    Node* root = ns.test_tree();
    std::cout << "result = " << ns.compute_tilt(root) << '\n';

    Solution s;
    TreeNode* root2 = s.test_tree();
    std::cout << "result2 = " << s.findTilt(root2) << '\n';
    return 0;
}
