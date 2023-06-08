class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int m = grid.size(), n= grid[0].size(), r = m-1, c= 0, cnt = 0;
        while(r>=0 and c<n){
            if(grid[r][c]<0){
                --r;
                cnt += n-c;
            }
            else
                c++;
        }
        return cnt;
    }
};