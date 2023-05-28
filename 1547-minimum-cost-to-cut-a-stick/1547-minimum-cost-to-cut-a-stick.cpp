class Solution {
public:
    int dp[102][102]={};
    int minCost(int n, vector<int>& cuts) {
        cuts.push_back(0);
        cuts.push_back(n);
        sort(cuts.begin(),cuts.end());
        int c=cuts.size();
        for(int i=c-2;i>=1;i--)
        {
            for(int j=1;j<=c-2;j++)
            {
                if(i>j)
                    continue;
                    int minCost=INT_MAX;
                    for(int index=i;index<=j;index++)
                    {
                        int cost=cuts[j+1]-cuts[i-1]+dp[i][index-1]+dp[index+1][j];
                        minCost=min(cost,minCost);
                    }
                dp[i][j]=minCost;
            }
        }
        return dp[1][c-2];
    }
};