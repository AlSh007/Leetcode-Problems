class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        int n=nums.size();
        vector<int> ans;
        priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> minh;
        for(int i=0;i<n;i++){
            mp[nums[i]]++;
        }
        for(auto it=mp.begin();it!=mp.end();it++){
            minh.push({it->second,it->first});
            if(minh.size()>k)
                minh.pop();
        }
        while(minh.size()){
            ans.push_back(minh.top().second);
            minh.pop();
        }
        return ans;
    }
};