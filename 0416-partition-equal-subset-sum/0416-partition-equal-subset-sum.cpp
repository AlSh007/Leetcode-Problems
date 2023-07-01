class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int totalSum = accumulate(begin(nums),end(nums),0),halfSum = totalSum/2;
        if(totalSum&1)
            return false;
        bool dp[halfSum+1];
        memset(dp,false,sizeof(dp));
        dp[0] = true;
        for(int num:nums)
            for(int j=halfSum;j>=num;j--){
                if(dp[j-num]) //if this sum already exists then we know that j is posibble
                    dp[j] = true;
            }
        return dp[halfSum];
        
    }
};