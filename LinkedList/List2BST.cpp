#include <iostream>
#include <vector>

using std::vector;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(NULL) {}
};

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};


class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return helper(nums, 0, nums.size()-1);
    }

    TreeNode* helper(vector<int>& nums, int l, int r) {
        if (l > r)
            return NULL;
        int mid = (l + r) / 2;
        TreeNode* node = new TreeNode(nums[mid]);
        node->left = helper(nums, l, mid-1);
        node->right = helper(nums, mid+1, r);
        return node;
    }

    TreeNode* sortedListToBST(ListNode* head) {
        vector<int> nums;
        while (head) {
            nums.push_back(head->val);
            head = head->next;
        }
        return helper(nums, 0, nums.size()-1);
    }

    void inorder(TreeNode* node) {
        if (node == NULL)
            return;
        inorder(node->left);
        std::cout << node->val << "\n";
        inorder(node->right);
    }

    void preorder(TreeNode* node) {
        if (node == NULL)
            return;
        std::cout << node->val << "\n";
        preorder(node->left);
        preorder(node->right);
    }
};

int main()
{
    // vector<int> nums {-10, -3, 0, 5, 9};
    vector<int> nums {4,6,8,10,12,14,16};
    Solution s;
    TreeNode* root = s.sortedArrayToBST(nums);
    std::cout << "PreOrder\n";
    s.preorder(root);
    std::cout << "\nInOrder\n";
    s.inorder(root);
    return 0;
}
