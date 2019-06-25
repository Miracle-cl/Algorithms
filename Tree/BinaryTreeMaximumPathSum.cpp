#include <iostream>

using namespace std;

// A binary tree node
struct TreeNode
{
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// This function returns overall maximum path sum in 'res'
// And returns max path sum going through root.
int findMaxUtil(TreeNode* root, int& res)
{
    //Base Case
    if (root == NULL)
        return 0;

    // l and r store maximum path sum going through left and
    // right child of root respectively
    int l = findMaxUtil(root->left, res);
    int r = findMaxUtil(root->right, res);

    // Max path for parent call of root. This path must
    // include at-most one child of root
    int max_single = max(max(l, r) + root->val, root->val);

    // Max Top represents the sum when the Node under
    // consideration is the root of the maxsum path and no
    // ancestors of root are there in max sum path
    int max_top = max(max_single, l + r + root->val);

    res = max(res, max_top); // Store the Maximum Result.

    return max_single;
}


int findMaxUnit2(TreeNode* node, int& res) {
    // same as findMaxUtil
    if (node == NULL)
        return 0;

    int left = std::max(0, findMaxUnit2(node->left, res));
    int right = std::max(0, findMaxUnit2(node->right, res));

    // int max_half = std::max(std::max(left, right) + node->val, node->val);
    // int max_top = std::max(max_half, left + right + node->val);
    res = std::max(res, left + right + node->val);
    return std::max(left, right) + node->val;
}

// Returns maximum path sum in tree with given root
int findMaxSum(TreeNode *root)
{
    // Initialize result
    int res = root->val;

    // Compute and return result
    findMaxUtil(root, res);
    return res;
}

class Solution {
public:
    int findMaxUnit(TreeNode* node, int& res) {
        if (node == NULL)
            return 0;

        int left = findMaxUnit(node->left, res);
        int right = findMaxUnit(node->right, res);

        int max_half = std::max(std::max(left, right) + node->val, node->val);
        int max_top = std::max(max_half, left + right + node->val);
        res = std::max(res, max_top);
        return max_half;
    }

    int maxPathSum(TreeNode* root) {
        int res = root->val;
        findMaxUnit(root, res);
        return res;
    }
};

// Driver program
int main()
{
    TreeNode* root = new TreeNode(-2);
    root->left = new TreeNode(-1);
    root->right = new TreeNode(4);

    Solution s;
    std::cout << "Max path sum is " << s.maxPathSum(root) << "\n";
    std::cout << "Max path sum is " << findMaxSum(root) << "\n";
    return 0;
}
