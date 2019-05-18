#include <iostream>
#include <string>
#include <vector>

using std::string;
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
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> res;
        vector<int> temp;
        dfs(root, res, temp);
        return res;
    }

    void dfs(TreeNode* node, vector<string>& res, vector<int>& temp) {
        if (node == nullptr)
            return;
        temp.push_back(node->val);
        if (node->left == nullptr && node->right == nullptr) {
            string2vector(res, temp);
        }
        dfs(node->left, res, temp);
        dfs(node->right, res, temp);
        temp.pop_back();
    }

    void string2vector(vector<string>& res, const vector<int>& temp) {
        string s;
        int length = temp.size() - 1;
        for (int i = 0; i <= length; i++) {
            s += std::to_string(temp[i]);
            if (i < length)
                s += "->";
        }
        res.push_back(s);
    }
};

class Solution1 {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> res;
        if (!root) return res;
        string path = std::to_string(root->val);
        dfs(root, res, path);
        return res;
    }

    void dfs(TreeNode* node, vector<string>& res, string path) {
        if (node == nullptr)
            return;
        if (node->left == nullptr && node->right == nullptr) {
            res.push_back(path);
            return;
        }
        if (node->left)
            dfs(node->left, res, path + "->" + std::to_string(node->left->val));
        if (node->right)
            dfs(node->right, res, path + "->" + std::to_string(node->right->val));
    }
};

int main()
{
    // string s;
    // for (int i = 0; i < 4; i++) {
    //     s += '0' + i;
    //     if (i < 3)
    //         s += "->";
    // }
    // std::cout << s << "\n";
    TreeNode* n1 = new TreeNode(1);
    TreeNode* n2 = new TreeNode(2);
    TreeNode* n3 = new TreeNode(3);
    TreeNode* n5 = new TreeNode(5);
    n1->left = n2;
    n1->right = n3;
    n2->right = n5;
    Solution1 solu;
    vector<string> res = solu.binaryTreePaths(n1);
    for (auto x: res) {
        std::cout << x << " ";
    }
    std::cout << "\n";
    return 0;
}
