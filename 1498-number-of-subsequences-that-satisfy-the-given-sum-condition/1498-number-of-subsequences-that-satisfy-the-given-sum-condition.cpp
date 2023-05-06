class Solution {
public:
    int numSubseq(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        int res=0,n=nums.size(),i=0,j=nums.size()-1,mod=1e9+7;
        vector<int> pows(n,1);
        for(int i=1;i<n;i++){
            pows[i]=pows[i-1]*2%mod;
        }
            while(i<=j){
            if(nums[i]+nums[j]>target)
                j--;
            else{
                res=(res+pows[j-i])%mod;
                i++;
            }
            }
        return res;
        }
};