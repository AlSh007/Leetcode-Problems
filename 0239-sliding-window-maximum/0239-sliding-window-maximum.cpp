class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n=nums.size();
        deque<int> dq;
        vector<int> ans;
        for(int left=0;left<n;left++){
            if(dq.front()== left-k)
                dq.pop_front();
            while(!dq.empty() and nums[dq.back()]<nums[left])
                dq.pop_back();
            dq.push_back(left);
            if(left-k+1>=0)
                ans.push_back(nums[dq.front()]);
        }
        return ans;
    }
};