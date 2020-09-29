#include <iostream>
#include <vector>
#include <unordered_map>
#include <iterator> // std::distance
#include <algorithm> // std::find

using std::vector;
using std::unordered_map;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};


class Solution {
    unordered_map<int, int> id_map;
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        if (inorder.empty())
            return nullptr;
        
        int n = inorder.size()-1;
        for (int i = 0; i <= n; i++)
            id_map[inorder[i]] = i;
        
        auto root = build(0, n, 0, n, inorder, postorder);
        return root;
    }
    
    TreeNode* build(int il, int ir, int pl, int pr, vector<int>& inorder, vector<int>& postorder) {
        if (il > ir)
            return nullptr;
        if (il == ir)
            return new TreeNode(inorder[il]);
        TreeNode* root = new TreeNode(postorder[pr]);
        int i = id_map[postorder[pr]];
        root->left = build(il, i-1, pl, pl+i-il-1, inorder, postorder);
        root->right = build(i+1, ir, pl+i-il, pr-1, inorder, postorder);
        return root;
    }
};


class Solution {
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        if (inorder.empty())
            return nullptr;
        int n = inorder.size()-1;
        auto root = build(0, n, 0, n, inorder, postorder);
        return root;
    }
    
    TreeNode* build(int il, int ir, int pl, int pr, vector<int>& inorder, vector<int>& postorder) {
        if (il > ir)
            return nullptr;
        if (il == ir)
            return new TreeNode(inorder[il]);
        TreeNode* root = new TreeNode(postorder[pr]);
        auto it = std::find(inorder.begin(), inorder.end(), postorder[pr]);
        int i = std::distance(inorder.begin(), it);
        root->left = build(il, i-1, pl, pl+i-il-1, inorder, postorder);
        root->right = build(i+1, ir, pl+i-il, pr-1, inorder, postorder);
        return root;
    }
};