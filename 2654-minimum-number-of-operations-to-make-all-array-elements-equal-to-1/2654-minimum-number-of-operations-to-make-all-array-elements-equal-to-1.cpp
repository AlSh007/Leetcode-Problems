class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n=nums.size();
        int t=INT_MAX,count=0;
        for(auto n:nums) if(n==1) count++;
        if(count>0) return n-count;
        for(int i=0;i<n;i++){
            int last=nums[i];
            for(int j=i+1;j<n;j++){
                last=__gcd(last,nums[j]);
                if(last==1){
                  t=min(t,j-i);
                    break;  
                } 
            }
        }
        if(t!=INT_MAX) return n-1+t;
        return -1;
    }
};