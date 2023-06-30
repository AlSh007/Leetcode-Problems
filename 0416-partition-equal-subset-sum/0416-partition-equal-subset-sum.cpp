class Solution {
public:
    int8_t dp[201][10001] = {[0 ... 200] = {[0 ... 10000] = -1}};  // all initialized to -1 (use dynamic vector to generalize to higher array size & possible sums)
    bool solve(vector<int>& nums,int sum,int i=0){
        if(sum==0)
            return true;
        int n = nums.size();
        if(i>=nums.size() or sum<0)
            return false;
        if (dp[i][sum] != -1)
            return dp[i][sum];
        return dp[i][sum] = solve(nums,sum-nums[i],i+1) || solve(nums,sum,i+1);
    }
    bool canPartition(vector<int>& nums) {
        int sum=0;
        for(int i=0;i<nums.size();i++){
            sum += nums[i];
        }
        if(sum & 1)
            return false;
        return solve(nums,sum/2);
    }
};