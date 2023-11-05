class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.extend([0,n])
        cuts.sort()
        dp = [[0]*len(cuts) for _ in cuts]
        
        for i in range(len(cuts) - 1, -1, -1):
            for j in range(i+2, len(cuts)):
                dp[i][j] = cuts[j] - cuts[i] + min(dp[i][k] + dp[k][j] for k in range(i+1, j))
        
        return dp[0][-1]