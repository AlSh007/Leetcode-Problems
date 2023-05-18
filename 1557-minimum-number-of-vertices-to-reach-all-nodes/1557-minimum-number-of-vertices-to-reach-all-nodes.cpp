class Solution {
public:
    vector<int> findSmallestSetOfVertices(int n, vector<vector<int>>& edges) {
        vector<int> seen(n);
        for(auto& e:edges){
            seen[e[1]]=1;
        }
        vector<int> ans;
        for(int i=0;i<n;i++)
        {
            if(seen[i]==0)
                ans.push_back(i);
        }
        return ans;
    }
};