class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        dp = [[1000]*(n+1) for _ in range(m + 1)]
        
        def solve(i, j):
            if i == m and j == n:
                return 0
            if i == m or j == n:
                return max(m - i, n - j)
            if dp[i][j] != 1000:
                return dp[i][j]
            
            if word1[i] == word2[j]:
                return solve(i + 1, j + 1)
            dp[i][j] = 1 + min(solve(i+1, j), solve(i, j+1))
            return dp[i][j]
            
        
        return solve(0,0)