#include <iostream>
#include <stdio.h>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    TreeNode* convertBST(TreeNode* root) {
        int v = 0;
        inorder_reverse(root, v);
        return root;
    }

    void inorder_reverse(TreeNode* root, int& v) {
        if (!root)
            return;
        inorder_reverse(root->right, v);
        v += root->val;
        root->val = v;
        inorder_reverse(root->left, v);
    }
};

// void recursionMiddleorderTraversal(TreeNode* root, int* sumn) {
//     if (root != NULL) {
//         recursionMiddleorderTraversal(root->right, sumn);
//         root->val += *sumn;
//         *sumn = root->val;
//         printf("%d\n", root->val);
//         recursionMiddleorderTraversal(root->left, sumn);
//     }
// }


int main()
{
    int sumn = 0;
    TreeNode* root = new TreeNode(5);
    root->left = new TreeNode(3);
    root->right = new TreeNode(7);
    root->left->left = new TreeNode(2);
    root->left->right = new TreeNode(4);
    root->right->left = new TreeNode(6);
    root->right->right = new TreeNode(8);
    // printf("Result: \n");
    // recursionMiddleorderTraversal(root, &sumn);
    return 0;
}
