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
    int widthOfBinaryTree(TreeNode* root) {
        if(!root)
            return 0;
        queue<pair<TreeNode*,int>> q;
        int maxWidth=1;
        q.push({root,0});
        while(!q.empty()){
            int l=q.front().second,r=q.back().second;
            maxWidth=max(maxWidth,r-l+1);
            
            for(int i=0,n=q.size();i<n;i++){
                auto it=q.front();
                int idx=it.second-l;
                q.pop();
                if(it.first->left){
                    q.push({it.first->left,(long long)2*idx+1});
                }
                if(it.first->right){
                    q.push({it.first->right,(long long)2*idx+2});
                }
            }
        }
        return maxWidth;
    }
};