class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2 or grid[0][0] == ')' or grid[-1][-1] == '(':
            return False
            
        # dp[j] = bitmask; bit b set means balance b is reachable at this cell
        dp = [0] * n
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    inc = 1  # balance 0
                else:
                    inc = (dp[j] if i > 0 else 0) | (dp[j - 1] if j > 0 else 0)
                dp[j] = inc << 1 if grid[i][j] == '(' else inc >> 1
        return dp[-1] & 1 == 1