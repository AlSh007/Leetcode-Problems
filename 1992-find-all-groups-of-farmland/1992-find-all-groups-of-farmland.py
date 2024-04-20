class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        group = []
        m, n = len(land), len(land[0])
        
        def dfs(row, col):
            if row < 0 or col < 0 or row >= m or col >= n or land[row][col] == 0:
                return (0, 0)
            
            land[row][col] = 0
            
            h_r1, h_c1 = dfs(row + 1, col)
            h_r2, h_c2 = dfs(row, col + 1)
            
            r1 = max(h_r1, h_r2, row)
            c1 = max(h_c1, h_c2, col)
            
            return (r1, c1)
        
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    x, y = dfs(i, j)
                    group.append([i, j, x, y])
                    
        return group