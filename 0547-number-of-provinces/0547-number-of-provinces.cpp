class Solution {
public:
    void dfs(int node,vector<vector<int>>& isConnected,vector<bool>& vis){
        vis[node] = true;
        for(int i=0;i<isConnected[node].size();i++){
            if(!vis[i] and isConnected[node][i])
                dfs(i,isConnected,vis);
        }
    }
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size(), ans = 0;
        vector<bool> visited(n,false);
        for(int i=0;i<n;i++){
            if(!visited[i]){
                ans++;
                dfs(i,isConnected,visited);
            }
        }
        return ans;
    }
};