class Solution {
public:
    bool dfs(int v,int c,vector<int>&vis,vector<int>&col,vector<vector<int>>& graph){
        vis[v]=1;
        col[v]=c;
        for(int child:graph[v]){
            if(vis[child]==0){
                if(!dfs(child,c^1,vis,col,graph))
                    return false;
            }
            else{
                if(col[v]==col[child]){
                    return false;
                }
            }
        }
        return true;
    }
    bool isBipartite(vector<vector<int>>& graph) {
        int n=graph.size();
        vector<int> vis(n),col(n);
        for(int i=0;i<n;i++){
            if(vis[i]==0 and dfs(i,0,vis,col,graph)==false)
                return false;
        }
        return true;
    }
};