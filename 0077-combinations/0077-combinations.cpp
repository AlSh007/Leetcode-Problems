class Solution {
public:
    void solve(int ind,int n,int k,vector<int>& current,vector<vector<int>>& ans){
        if(current.size()==k)
        {
            ans.push_back(current);
            return;
        }
        for(int i=ind;i<n+1;i++){
            current.push_back(i);
            solve(i+1,n,k,current,ans);
            current.pop_back();
        }
    }
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> ans;;
        vector<int> current;
        solve(1,n,k,current,ans);
        return ans;
    }
};