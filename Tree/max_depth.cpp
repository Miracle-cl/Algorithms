#include <iostream>
#include <queue>
// #include <stdio.h>

using std::queue;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == NULL)
            return 0;
        int ll = maxDepth(node->left);
        int rr = maxDepth(node->right);
        return 1 + max(ll, rr);
    }
};

class SolutionQueue {
public:
    int maxDepth(TreeNode* root) {
        if (root == NULL)
            return 0;

        queue<TreeNode *> q;
        q.push (root);
        q.push(NULL);
        int count = 0;
        while(q.size()!=0)
        {
            root= q.front();
            q.pop();
            if (root == NULL)
            {
                count++;
                if (q.size()!=0)
                    q.push(NULL);
            }

            if (root)
            {
                if (root->left)
                    q.push(root->left);
                if (root->right)
                    q.push(root->right);
            }
        }
        return count;
    }
};
