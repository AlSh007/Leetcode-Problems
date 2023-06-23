class Solution {
public:
    int longestArithSeqLength(vector<int>& nums) {
        int res=2,n=nums.size();
        vector<vector<int>> dp(n,vector<int>(2000,0));
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                int diff = nums[j] - nums[i] + 1000;
                dp[j][diff] = max(dp[i][diff]+1,2);
                res = max(res,dp[j][diff]);
            }
        }
        return res;
    }
};