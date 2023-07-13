class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph(numCourses);
        vector<int> inDegree(numCourses,0);
        for(auto edge:prerequisites){
            graph[edge[1]].push_back(edge[0]);
            inDegree[edge[0]]++;
        }
        int count = 0;
        queue<int> q;
        for(int i=0;i<numCourses;i++){
            if(inDegree[i]==0)
                q.push(i);
        }
        while(!q.empty()){
            auto temp = q.front();
            q.pop();
            ++count;
            for(auto v: graph[temp]){
                if(--inDegree[v]==0){
                    q.push(v);
                }
            }
        }
        return count == numCourses;
    }
};