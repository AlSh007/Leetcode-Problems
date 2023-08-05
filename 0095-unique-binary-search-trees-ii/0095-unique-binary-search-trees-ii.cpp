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
    vector<TreeNode*> generateBST(int start,int end){
            vector<TreeNode*> res;

        if(start>end)
            return {NULL};
        if(start==end) return {new TreeNode(start)};
        for(int i=start;i<=end;i++){
            vector<TreeNode*> left=generateBST(start,i-1),right=generateBST(i+1,end);
            for(auto l:left){
                for(auto r:right){
                    res.push_back(new TreeNode(i,l,r));
                }
            }
        }
        return res;
    }
    vector<TreeNode*> generateTrees(int n) {
        return generateBST(1,n);
    }
};