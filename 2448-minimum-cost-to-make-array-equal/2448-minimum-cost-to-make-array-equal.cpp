class Solution {
public:
    long long minCost(vector<int>& nums, vector<int>& cost) {
        long long l=1,r=1000000,res = f(nums,cost,1),mid;
        while(l<r){
            mid = (l+r)/2;
            long long res1 = f(nums,cost,mid), res2 = f(nums,cost,mid+1);
            res = min(res1,res2);
            if(res1<res2)
                r = mid;
            else
                l = mid + 1;
        }
        return res;
    }
    long long f(vector<int>& nums,vector<int>&cost,int mid){
        long long res = 0;
        for(int i=0;i<nums.size();i++)
            res += 1L*abs(nums[i] - mid)*cost[i];
        return res;
    }
};