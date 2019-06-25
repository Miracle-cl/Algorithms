#include <iostream>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    bool isBalanced(TreeNode* root) {
        // if (root == NULL)
        if (!root)
            return true;
        int lh = cal_height(root->left);
        int rh = cal_height(root->right);
        if (abs(lh - rh) > 1)
            return false;
        else
            return isBalanced(root->left) && isBalanced(root->right);
    }

    int cal_height(TreeNode* node) {
        if (!node)
            return 0;
        int lh = cal_height(node->left);
        int rh = cal_height(node->right);
        return 1 + std::max(lh, rh);
    }
};

int main()
{
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(2);
    root->right = new TreeNode(4);
    root->left->left = new TreeNode(1);
    Solution s;
    int h = s.height(root);
    std::cout << h << "\n";
    return 0;
}
