class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        int top=0,bottom=n-1,left=0,right=n-1;
        int val=0;
        vector<vector<int>> ans(n,vector<int>(n));
        
        while(top<=bottom and left<=right){
            for(int col=left;col<=right;col++){
                ans[top][col]=++val;
            }
            for(int row=top+1;row<=bottom;row++){
                ans[row][right]=++val;
            }
            for(int col=right-1;col>=left;col--){
                ans[bottom][col]=++val;
            }
            for(int row=bottom-1;row>top;row--){
                ans[row][left]=++val;
            }
            top++;
            right--;
            left++;
            bottom--;
        }
        return ans;
    }
};