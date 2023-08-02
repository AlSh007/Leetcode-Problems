class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> cur = {};
        backtrack(nums,ans,cur);
        return ans;
    }
    void backtrack(vector<int>& nums,vector<vector<int>>& ans,vector<int>& cur){
        if(cur.size()==nums.size()){
            ans.push_back(cur);
            return;
        }
        for(int num:nums){
            if(find(cur.begin(),cur.end(),num) == cur.end()){
                cur.push_back(num);
                backtrack(nums,ans,cur);
                cur.pop_back();
            }
        }
    }
};