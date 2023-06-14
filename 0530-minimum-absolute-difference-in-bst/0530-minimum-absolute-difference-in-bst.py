/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    
    int minDiff = INT_MAX;
    TreeNode* prev = NULL;
    void inorderTraversal(TreeNode* node){
        if(node == nullptr)
            return;
        inorderTraversal(node -> left);
        if(prev){
            minDiff = min(minDiff, node->val - prev->val);
        }
        prev = node; //this makes sure that we have node to compare with left or right values
        inorderTraversal(node->right);
    }
    int getMinimumDifference(TreeNode* root) {
        inorderTraversal(root);
        return minDiff;
    }
};