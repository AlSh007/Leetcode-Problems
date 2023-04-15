class Solution {
public:
    int help(int i,vector<vector<int>>& piles,int k,vector<vector<int>>& dp){
        if(dp[i][k]>0)
            return dp[i][k];
        if(i==piles.size() or k==0)
            return 0;
        int res=help(i+1,piles,k,dp),curVal=0;
        for(int j=0;j<piles[i].size() and j<k;j++){
            curVal+=piles[i][j];
            res=max(res,help(i+1,piles,k-j-1,dp)+curVal);
        }
        dp[i][k]=res;
        return res;
    }
    int maxValueOfCoins(vector<vector<int>>& piles, int k) {
        int n=piles.size();
        vector<vector<int>> dp(n+1,vector<int>(k+1,0));
        return help(0,piles,k,dp);
    }
};