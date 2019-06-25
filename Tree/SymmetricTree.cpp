#include <iostream>
#include <queue>
// #include <stdio.h>


// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (root == NULL)
            return true;
        return helper(root->left, root->right);
    }

    bool helper(TreeNode* node1, TreeNode* node2) {
        if (node1 == NULL && node2 == NULL)
            return true;
        if (node1 == NULL || node2 == NULL)
            return false;
        bool cond1 = node1->val == node2->val;
        bool cond2 = helper(node1->left, node2->right);
        bool cond3 = helper(node1->right, node2->left);
        return cond1 && cond2 && cond3;
    }

    bool isSymmetric_loop(TreeNode* root) {
        if (root == NULL)
            return true;
        TreeNode* n1 = root->left;
        TreeNode* n2 = root->right;
        if (n1 == NULL && n2 == NULL)
            return true;
        if (n1 == NULL || n2 == NULL)
            return false;
        std::queue<TreeNode*> q1;
        std::queue<TreeNode*> q2;
        q1.push(n1);
        q2.push(n2);
        while (!q1.empty() && !q2.empty()) {
            TreeNode* n1 = q1.front();
            TreeNode* n2 = q2.front();
            q1.pop();
            q2.pop();
            if ((!n1 && n2) || (n1 && !n2))
                return false;
            if (n1 && n2) {
                if (n1->val != n2->val)
                    return false;
                q1.push(n1->left);
                q1.push(n1->right);
                q2.push(n2->right);
                q2.push(n2->left);
            }
        }
        return true;
    }
};

int main()
{
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(2);
    root->left->left = new TreeNode(3);
    root->left->right = new TreeNode(4);
    root->right->left = new TreeNode(4);
    root->right->right = new TreeNode(3);

    Solution s;
    bool r1 = s.isSymmetric(root);
    bool r2 = s.isSymmetric_loop(root);
    std::cout << "Result: " << r1 << ", " << r2 << "\n";
    return 0;
}
