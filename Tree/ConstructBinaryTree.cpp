#include <iostream>
#include <vector>
#include <unordered_map>

using std::vector;
using std::unordered_map;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return helper(preorder, 0, preorder.size()-1, inorder, 0, inorder.size()-1);
    }

    TreeNode* helper(vector<int>& preorder, int lp, int rp,
                     vector<int>& inorder, int li, int ri) {
        if (lp > rp || li > ri)
            return NULL;
        TreeNode* node = new TreeNode(preorder[lp]);
        int i = 0;
        for (i = li; i <= ri; i++) {
            if (inorder[i] == preorder[lp])
                break;
        }
        node->left = helper(preorder, lp+1, lp+i-li, inorder, li, i-1);
        node->right = helper(preorder, lp+i-li+1, rp, inorder, i+1, ri);
        return node;
    }
};

class Solution1 {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        std::unordered_map<int, int> inorder_map;
        for (int i = 0; i < inorder.size(); i++)
            inorder_map[inorder[i]] = i;
        return helper(preorder, 0, preorder.size()-1, inorder, 0, inorder.size()-1, inorder_map);
    }

    TreeNode* helper(vector<int>& preorder, int lp, int rp, vector<int>& inorder, int li, int ri, unordered_map<int, int>& inorder_map) {
        if (lp > rp || li > ri)
            return NULL;
        TreeNode* node = new TreeNode(preorder[lp]);
        int i = inorder_map[preorder[lp]];
        node->left = helper(preorder, lp+1, lp+i-li, inorder, li, i-1, inorder_map);
        node->right = helper(preorder, lp+i-li+1, rp, inorder, i+1, ri, inorder_map);
        return node;
    }
};

class SolutionPrePost {
public:
    TreeNode* constructFromPrePost(vector<int>& pre, vector<int>& post) {
        int preid = 0;
        int length = pre.size();
        return helper(pre, post, &preid, 0, length-1, length);
    }

    TreeNode* helper(vector<int>& pre, vector<int>& post, int* preid, int begin, int end, int length) {
        // e: pre, t:post, s:start, e:end
        if (*preid >= length || begin > end)
            return NULL;
        TreeNode* node = new TreeNode(pre[*preid]);
        (*preid)++; // same as ++*preid
        if (begin == end)
            return node;
        int i = begin;
        for (; i <= end; i++) {
            if (pre[*preid] == post[i])
                break;
        }
        if (i <= end) {
            node->left = helper(pre, post, preid, begin, i, length);
            node->right = helper(pre, post, preid, i+1, end, length);
        }
        // std::cout << *preid << "," << begin << "," << end << "\n";
        return node;
    }
};


int main()
{
    // std::vector<int> preorder {3,9,20,15,7};
    // std::vector<int> inorder {9,3,15,20,7};
    // Solution1 solu;
    // TreeNode* root = solu.buildTree(preorder, inorder);

    std::vector<int> pre {1,2,4,5,3,6,7};
    std::vector<int> post {4,5,2,6,7,3,1};
    SolutionPrePost sprepost;
    TreeNode* root = sprepost.constructFromPrePost(pre, post);
    // std::cout << root->val << "," << root->left->val << "," << root->right->val << "\n";
    // TreeNode* root1 = root->left;
    // TreeNode* root2 = root->right;
    // std::cout << root1->val << "," << root1->left->val << "," << root1->right->val << "\n";
    // std::cout << root2->val << "," << root2->left->val << "," << root2->right->val << "\n";
    return 0;
}
