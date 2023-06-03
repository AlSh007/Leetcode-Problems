class Solution {
public:
    int numOfMinutes(int n, int headID, vector<int>& manager, vector<int>& informTime) {
        unordered_map<int,vector<int>> m;
        queue<pair<int,int>> q;
        q.push({headID,0});
        for(int i=0;i<manager.size();i++){
            m[manager[i]].push_back(i);
        }
        int maxTimeTaken = 0;
        while(!q.empty()){
            int n = q.size();
            for(int i=0;i<n;i++){
                int head = q.front().first;
                int timeTaken = q.front().second;
                q.pop();
                int dur = informTime[head] + timeTaken;
                maxTimeTaken = max(maxTimeTaken, dur);
                for(auto it: m[head]){
                    q.push({it,dur});
                }
            }
        }
        return maxTimeTaken;
    }
};