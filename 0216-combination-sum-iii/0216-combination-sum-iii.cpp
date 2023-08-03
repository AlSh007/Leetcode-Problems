class Solution {
public:
            
    void backtrack(vector<vector<int>>& ans,vector<int> cur,int k,int n){
        if(cur.size() == k and n==0){
            ans.push_back(cur);
            return;
        }
        for(int i=cur.empty()?1:cur.back()+1;i<10;i++){
            if(n-i<0)
                break;
            cur.push_back(i);
            backtrack(ans,cur,k,n-i);
            cur.pop_back();
        }
    }
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> ans;
        vector<int> currComb;
        backtrack(ans,currComb,k,n);
        return ans;
    }
};