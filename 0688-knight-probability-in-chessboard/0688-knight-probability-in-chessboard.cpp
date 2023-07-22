class Solution {
public:
    double find(int n,int k,int r,int c,vector<vector<vector<double>>>& dp)
    {
        if(r<0 or c<0 or r>=n or c>=n)
        {
            return 0;
        }
        if(k==0) return 1;
        if(dp[r][c][k]) return dp[r][c][k];
        double p=find(n,k-1,r+1,c+2,dp)+find(n,k-1,r-1,c-2,dp)+
            find(n,k-1,r+2,c+1,dp)+find(n,k-1,r-2,c-1,dp)+
            find(n,k-1,r+1,c-2,dp)+find(n,k-1,r-1,c+2,dp)+
            find(n,k-1,r+2,c-1,dp)+find(n,k-1,r-2,c+1,dp);
        p/=8;
        dp[r][c][k]=p;
        return p;
    }
    double knightProbability(int n, int k, int row, int column) {
        vector<vector<vector<double>>> dp(n,vector<vector<double>>(n,vector<double>(k+1)));
        return find(n,k,row,column,dp);
    }
};