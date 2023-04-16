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
    TreeNode* replaceValueInTree(TreeNode* root) {
        if (root == NULL) {
        return NULL;
    }
    queue<TreeNode*> q;
    root->val=0;
    q.push(root);
    while(!q.empty()){
        int n=q.size(),sum=0;
        vector<TreeNode*> buf;
        while(n--){
            auto node=q.front();
            q.pop();
            buf.push_back(node);
            if(node->left) {
                sum+=node->left->val;
                q.push(node->left);
            }
            if(node->right){
                sum+=node->right->val;
                q.push(node->right);
            }
        }
        for(auto node: buf){
            int t=sum;
            if(node->left) t-=node->left->val;
            if(node->right) t-=node->right->val;
            if(node->left) node->left->val=t;
            if(node->right) node->right->val=t;
        }
    }
        return root;
    }
};