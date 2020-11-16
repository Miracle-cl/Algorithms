#include <iostream>
#include <vector>
#include <algorithm>


using std::vector;


struct SegNode {
    int start;
    int end;
    int sum;
    SegNode* left;
    SegNode* right;
    SegNode(int s, int e, int v): start(s), end(e), sum(v), left(NULL), right(NULL) {}
    SegNode(int s, int e, int v, SegNode* l, SegNode* r): start(s), end(e), sum(v), left(l), right(r) {}
};


class SegTree {
public:
    SegNode* build(int s, int e, int v) {
        if (s == e)
            return new SegNode(s, e, v);
        int mid = (s + e) / 2;
        SegNode* left = build(s, mid, v);
        SegNode* right = build(mid+1, e, v);
        return new SegNode(s, e, v, left, right);
    }

    void update(SegNode* root, int i, int val) {
        root->sum += val;
        if (root->start == i && root->end == i)
            return;
        int mid = (root->start + root->end) / 2;
        if (i <= mid)
            update(root->left, i, val);
        else
            update(root->right, i, val);
        return;
    }

    int query(SegNode* root, int s, int e) {
        if (root->start == s && root->end == e)
            return root->sum;
        int mid = (root->start + root->end) / 2;
        if (e <= mid)
            return query(root->left, s, e);
        if (mid < s)
            return query(root->right, s, e);
        return query(root->left, s, mid) + query(root->right, mid+1, e);
    }
};


class Solution {
public:
    int createSortedArray(vector<int>& instructions) {
        constexpr int mode = 1000000007; 
        int n = *std::max_element(instructions.begin(), instructions.end());
        SegTree st;
        SegNode* root = st.build(0, 1+n, 0);
        long long cost = 0;
        for (int i = 0; i < instructions.size(); i++) {
            int smaller = st.query(root, 0, instructions[i]-1);
            int larger = st.query(root, instructions[i]+1, n+1);
            cost += std::min(smaller, larger);
            st.update(root, instructions[i], 1);
            // std::cout << smaller << ' ' << larger << '\n';
        }
        return cost % mode;
    }
};


int main () 
{
    vector<int> instructions {1,3,3,3,2,4,2,1,2};
    Solution solu;
    int res = solu.createSortedArray(instructions);
    std::cout << res << '\n';
    return 0;
}
