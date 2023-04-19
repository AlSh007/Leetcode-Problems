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
    int pathLength=0;
    void dfs(TreeNode* root,bool goLeft,int steps){
        if(root==NULL)
            return;
        pathLength=max(pathLength,steps);
        if(goLeft){
            dfs(root->left,false,steps+1);
            dfs(root->right,true,1);
        }
        else{
            dfs(root->left,false,1);
            dfs(root->right,true,steps+1);
            
        }
    }
    int longestZigZag(TreeNode* root) {
        dfs(root,false,0);
        return pathLength;
    }
};