static class DSU{
    vector<int> parent,rank;
    public:
    DSU(int n){
        parent.resize(n);
        rank.resize(n,0);
        for(int i=0;i<n;i++)
            parent[i]=i;
    }
    int find(int x){
        return parent[x]=x==parent[x]?x:find(parent[x]);
    }
    bool Union(int x,int y){
        int xset=find(x),yset=find(y);
        if(xset!=yset){
            rank[xset]<rank[yset]?parent[xset]=yset:parent[yset]=xset;
            rank[xset]+=rank[xset]==rank[yset];
            return true;
        }
        return false;
    }
};

class Solution {
public:
    vector<bool> distanceLimitedPathsExist(int n, vector<vector<int>>& edgeList, vector<vector<int>>& queries) {
        DSU dsu(n);
        for(int i=0;i<queries.size();i++)
            queries[i].push_back(i); 
        
        sort(queries.begin(),queries.end(),[](auto &l,auto &r){
            return l[2]<r[2];
        });
        sort(edgeList.begin(),edgeList.end(),[](auto &l,auto &r){
            return l.back()<r.back();
        });
        int i=0;
        vector<bool> result(queries.size());
        for(auto &q:queries){
            while(i<edgeList.size() and edgeList[i][2]<q[2])
            {
                dsu.Union(edgeList[i][0],edgeList[i][1]);
                i++;
            }
            result[q.back()]=dsu.find(q[0])==dsu.find(q[1]);
        }
        return result;
    }
};