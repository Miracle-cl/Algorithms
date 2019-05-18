#include <iostream>
#include <queue>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

void bfs(TreeNode* root) {
    if (root == NULL) {
        std::cout  << "NULL \n";
        return;
    }

    std::queue<TreeNode*> qq;
    qq.push(root);
    while (!qq.empty()) {
        TreeNode* node = qq.front();
        qq.pop();
        std::cout  << node->val << "\n";
        if (node->left != NULL)
            qq.push(node->left);
        if (node->right != NULL)
            qq.push(node->right);
    }
}

int main()
{
    // TreeNode* root = NULL;
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(2);
    root->left->left = new TreeNode(3);
    //root->left->right = new TreeNode(4);
    root->right->left = new TreeNode(4);
    root->right->right = new TreeNode(3);

    bfs(root);

    return 0;
}
