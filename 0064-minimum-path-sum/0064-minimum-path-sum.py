class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[-1]*len(grid[0]) for _ in range(len(grid))]
        m = len(grid)
        n = len(grid[0])
        def solve(i,j):
            if i<0 or j<0: 
                return inf
            if i == 0 and j == 0:
                return grid[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            ans = grid[i][j] + min(solve(i-1,j),solve(i,j-1))
            dp[i][j] = ans
            return ans
        
        
        ans = solve(m-1,n-1)
        return ans