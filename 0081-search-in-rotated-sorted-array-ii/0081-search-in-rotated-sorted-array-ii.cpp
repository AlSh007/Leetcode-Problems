class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int l = 0,r = nums.size()-1;
        while(l<=r){
            int mid = l+(r-l)/2;
            if(nums[mid]==target)
                return true;
            if(nums[mid]==nums[l] and nums[mid]==nums[r])
            {
                l++;
                r--;
            }
            else if(nums[l]<=nums[mid]){
                if(nums[mid]>target and nums[l]<=target){
                    r=mid-1;
                }
            else{
                l=mid+1;
            }
            }
            else{
                  if((nums[mid]<target) and nums[r]>=target){
                      l=mid+1;
                  }
                else{
                    r=mid-1;
                }
            }
                
        }
        return false;
    }
};