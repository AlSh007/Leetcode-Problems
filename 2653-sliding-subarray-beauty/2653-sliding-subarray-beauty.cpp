class Solution {
public:
    vector<int> getSubarrayBeauty(vector<int>& nums, int k, int x) {
        vector<int> res;
        multiset<int> ms;
        int n=nums.size(),j=0;
        for(int i=0;i<n;i++){
            if(nums[i]<0) ms.insert(nums[i]);
            if(i-j+1==k){
                if(ms.size()<x) res.push_back(0);
                else res.push_back(*next(ms.begin(),x-1));
                if(nums[j]<0) ms.erase(ms.find(nums[j]));
                j++;
            }
        }
        return res;
    }
};