class Solution {
public:
    int solve(int i, int prev, vector<int>& arr1, vector<int>& arr2, vector<vector<int>>& dp){
        if(i==arr1.size())
            return 0;
        int ind = upper_bound(arr2.begin(),arr2.end(),prev) - arr2.begin();
        if(dp[i][ind]!= -1)
            return dp[i][ind];
        if(ind == arr2.size() and arr1[i]<= prev)
            return dp[i][ind] = 1e9;
        int pick = 1e9;
        int npick = 1e9;
        if(ind != arr2.size()) pick = 1+solve(i+1,arr2[ind],arr1,arr2,dp);
        if(arr1[i]>prev) npick = solve(i+1,arr1[i],arr1,arr2,dp);
        return dp[i][ind] = min(pick,npick); 
    }
    int makeArrayIncreasing(vector<int>& arr1, vector<int>& arr2) {
        sort(arr2.begin(),arr2.end());
        vector<vector<int>> dp(arr1.size(),vector<int>(arr2.size()+1,-1));
        int ans = solve(0, -1, arr1, arr2, dp);
        return ans == 1e9 ? -1 : ans;
    }
};