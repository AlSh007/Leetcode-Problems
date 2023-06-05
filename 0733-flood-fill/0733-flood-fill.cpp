class Solution {
public:
    void dfs(int i,int j,vector<vector<int>>& image,int color,int sameColor){
        if(i<0 or j<0 or i>=image.size() or j>=image[0].size() or image[i][j]!=sameColor or image[i][j]==color)
            return;
        image[i][j] = color;
        dfs(i+1,j,image,color,sameColor);
        dfs(i-1,j,image,color,sameColor);
        dfs(i,j+1,image,color,sameColor);
        dfs(i,j-1,image,color,sameColor);
    }
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        int sameColor = image[sr][sc];
        dfs(sr,sc,image,color,sameColor);
        return image;
    }
};