class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int left = 0,right = 0;
        int ans = INT_MAX,n=nums.size(),sum = 0;
        while(right<n){
               sum += nums[right++];
            while(sum >= target){
                ans = min(ans,right-left);
                sum -= nums[left++];
            }
        }
        return ans == INT_MAX ? 0: ans;  
    }
};