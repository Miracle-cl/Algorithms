#include <iostream>
#include <stack>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

void dfs(TreeNode* root) {
    if (root == NULL) {
        std::cout << "NULL\n";
        return;
    }

    std::stack<TreeNode*> ss;
    ss.push(root);
    while (!ss.empty()) {
        TreeNode* node = ss.top();
        ss.pop();
        std::cout << node->val << "\n";
        if (node->right)
            ss.push(node->right);
        if (node->left)
            ss.push(node->left);
    }
}

void dfs_recursion(TreeNode* root) {
    if (root)
        std::cout << root->val << "\n";
    else
        return;
    dfs_recursion(root->left);
    dfs_recursion(root->right);
}

int main()
{
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(8);
    root->left->left = new TreeNode(3);
    root->left->right = new TreeNode(6);
    root->left->left->left = new TreeNode(4);
    root->left->left->right = new TreeNode(5);
    root->right->left = new TreeNode(9);
    root->right->right = new TreeNode(12);
    root->right->left->left = new TreeNode(10);
    root->right->left->right = new TreeNode(11);

    std::cout << "Stack-loop:\n";
    dfs(root);
    std::cout << "Recursion:\n";
    dfs_recursion(root);
    return 0;
}
