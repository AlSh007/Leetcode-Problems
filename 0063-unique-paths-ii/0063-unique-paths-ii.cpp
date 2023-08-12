class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = size(obstacleGrid),n=size(obstacleGrid[0]);;
        vector<vector<int>> dp(m+1,vector<int>(n+1,0));
        dp[0][1]=1; //this is to make sure that the first point in the actual grid has one way to reach there
        			// dp[i][j] = sum of unique paths for top and left cell (cells from which we reach current one)

        for(int i=1;i<=m;i++){
            for(int j=1;j<=n;j++){
                dp[i][j] = !obstacleGrid[i-1][j-1]?dp[i-1][j]+dp[i][j-1]:0;
            }
        }
        return dp[m][n];
    }
};