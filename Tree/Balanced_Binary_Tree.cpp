/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 
class Solution {
public:
    int height(TreeNode* node) {
        if (!node)
            return 0;
        int lh = height(node->left);
        int rh = height(node->right);
        return 1 + max(lh, rh);
    }

    bool isBalanced(TreeNode* root) {
        if (!root)
            return true;
        while (root->left || root->right) {
            int lh = height(root->left);
            int rh = height(root->right);
            if (abs(lh - rh) > 1)
                return false;
            else
                return isBalanced(root->left) && isBalanced(root->right);
        }
        return true;
    }
};
