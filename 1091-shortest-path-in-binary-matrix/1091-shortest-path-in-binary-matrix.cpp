class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        if(grid.empty() or grid[0][0]!=0)
            return -1;
        int m = grid.size();
        int n = grid[0].size();
        if(grid[0][0]==0 and m==1 and n==1)
            return 1;
        int steps = 0;
        vector<int> dir{0,1,0,-1,0,1,1,-1,-1,1};
        queue<pair<int,int>> q;
        q.push(make_pair(0,0));
        grid[0][0] = 1;
        while(!q.empty()){
            steps++;
            int size = q.size();
            for(int i = 0;i< size ; i++){
                auto cord  = q.front();
                q.pop();
                for(int i=0;i<9;i++){
                    int row = cord.first + dir[i];
                    int col = cord.second + dir[i+1];
                    if(row< m and row>=0 and col<n and col>=0 and grid[row][col]!=1){
                        if(row==m-1 and col==n-1)
                            return steps + 1;
                        q.push({row,col});
                        grid[row][col] = 1;
                    }
                }
            }
        }
        return -1;
    }
};