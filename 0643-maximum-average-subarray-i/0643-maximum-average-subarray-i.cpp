class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int i=0;
        double ans = INT_MIN, curSum = 0;
        for(int i=0;i<nums.size();i++){
            if(i<k)
                curSum += nums[i];
            else{
                ans = max(ans,curSum);
                curSum += nums[i] - nums[i-k];
            }
        }
        ans = max(ans,curSum);
        return ans/k;
    }
};