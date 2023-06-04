class Solution {
public:
    int parent[201];
    int findCircleNum(vector<vector<int>>& m) {
        int i,j,n=m.size(),groups = 0;
        make_set(n);
        
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                if(m[i][j])
                union_set(i,j);
            }
        }
        for(int i=0;i<n;i++){
            if(i == parent[i])
                groups++;
        }
        return groups;
    }
    private:
    void make_set(int n){
        for(int i=0;i<n;i++){
            parent[i]=i;
        }
    }
    int find_set(int v){
        if(v==parent[v])
            return v;
        return parent[v]=find_set(parent[v]);
    }
    void union_set(int i,int j){
        i = find_set(i);
        j = find_set(j);
        if(i!=j)
            parent[j]=i;
    }
};
