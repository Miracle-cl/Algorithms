#include <iostream>
#include <vector>

using std::vector;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    bool hasPathSum(TreeNode* root, int sum) {
        if (!root) return false;
        if (!root->left && !root->right) return (sum == root->val);
        int new_sum = sum - root->val;
        return hasPathSum(root->left, new_sum) || hasPathSum(root->right, new_sum);
    }

    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<int> temp;
        vector<vector<int>> res;
        dfs(root, sum, temp, res);
        return res;
    }

    void dfs(TreeNode* node, int sum, vector<int>& temp, vector<vector<int>>& res) {
        if (!node)
            return;
        temp.push_back(node->val);

        if (node->left) {
            dfs(node->left, sum-node->val, temp, res);
            temp.pop_back();
        }
        if (node->right) {
            dfs(node->right, sum-node->val, temp, res);
            temp.pop_back();
        }
        if (!node->left && !node->right && sum == node->val) {
            res.push_back(temp);
            return;
        }
    }
};

int main()
{
    TreeNode* root = new TreeNode(5);
    root->left = new TreeNode(4);
    root->left->left = new TreeNode(11);
    root->left->left->left = new TreeNode(7);
    root->left->left->right = new TreeNode(2);
    root->right = new TreeNode(8);
    root->right->left = new TreeNode(13);
    root->right->right = new TreeNode(4);
    root->right->right->left = new TreeNode(5);
    root->right->right->right = new TreeNode(1);

    Solution s;
    vector<vector<int>> res = s.pathSum(root, 22);
    for (auto n : res) {
        for (auto x : n) {
            std::cout << x << " ";
        }
        std::cout << "\n";
    }
    return 0;
}
