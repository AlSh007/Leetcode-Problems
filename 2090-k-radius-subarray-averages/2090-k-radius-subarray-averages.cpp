class Solution {
public:
    vector<int> getAverages(vector<int>& nums, int k) {
        long n = nums.size(), len = 2*k + 1, sum = 0;
        vector<int> ans(n,-1);
        for(int i=0;i<n;i++){
            sum += nums[i];
            if(i-len>=0)
                sum -= nums[i - len];
            if(i >= len - 1)
                ans[i-k] = sum/len;
        }
        return ans;
    }
};