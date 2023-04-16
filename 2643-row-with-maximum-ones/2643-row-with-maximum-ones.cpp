class Solution {
public:
    vector<int> rowAndMaximumOnes(vector<vector<int>>& mat) {
        int maxOnes=0;
        vector<int> ans;
        ans.push_back(0);
        ans.push_back(0);
        for(int i=0;i<mat.size();i++){
            int countOne=0;
            for(int j=0;j<mat[0].size();j++){
                if(mat[i][j]==1)
                    countOne+=1;
            }
            if(countOne>maxOnes)
            {
                ans.clear();
                maxOnes=countOne;
                ans.push_back(i);
                ans.push_back(maxOnes);
            }
        }
        return ans;
    }
};