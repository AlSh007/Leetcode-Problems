class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[-1]*n for _ in range(n)]
        dp[n-1] = triangle[n-1]
        for i in range(n-2,-1,-1):
            for j in range(i+1):
                lower_left = triangle[i][j] + dp[i+1][j]
                lower_right = triangle[i][j] + dp[i+1][j+1]
                dp[i][j] = min(lower_left,lower_right)
                
        return dp[0][0]