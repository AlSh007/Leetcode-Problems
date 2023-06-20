class Solution {
public:
    vector<int> getAverages(vector<int>& nums, int k) {
        int n = nums.size(), len = 2*k + 1;
        vector<int> ans(n,-1);
        if(n<len)
            return ans;
        vector<long> sum(n+1);
        for(int i=0;i<n;i++)
            sum[i+1] = sum[i] + nums[i];
        for(int i=k;i + k<n;i++){
            ans[i] = (sum[i+k+1] - sum[i-k])/len;
        }
        return ans;
    }
};