class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        mod = 10**9 + 7
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        dp = [[0]*n for i in range(m)]
        
        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]
            
            ans = 1
            
            for dx,dy in directions:
                x, y = i+dx, j+dy
                if 0<=x<m and 0<=y<n and grid[x][y] < grid[i][j]:
                    ans += dfs(x, y)%mod
            dp[i][j] = ans
            return ans
        return sum(dfs(i,j) for i in range(m) for j in range(n))%mod
        