class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        if (m + n -1) % 2 or grid[0][0] == ')' or grid[-1][-1] == '(':
            return False

        memo = {}

        def dfs(row, col, balance):
            if row >= m or col >= n:
                return False
            
            balance += 1 if grid[row][col] == '(' else -1

            if balance < 0:
                return False
            
            if row == m - 1 and col == n - 1:
                return balance == 0
            
            key = (row, col, balance)

            if key not in memo:
                memo[key] = (dfs(row + 1, col, balance) or dfs(row, col + 1, balance))
                return memo[key]
        
        return dfs(0, 0, 0)