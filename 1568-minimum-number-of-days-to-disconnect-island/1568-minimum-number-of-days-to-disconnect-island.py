class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def count_islands():
            visited = set()
            count = 0
            
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        explore_island(i, j, visited)
                        count += 1
            
            return count
        
        def explore_island(i, j, visited):
            if (
                i < 0
                or i >= rows
                or j < 0
                or j >= cols
                or grid[i][j] == 0
                or (i, j) in visited
            ):
                return
            
            visited.add((i, j))
            for di, dj in ([0, 1], [0, -1], [1, 0], [-1, 0]):
                explore_island(i + di, j + dj, visited)
        
        if count_islands() != 1:
            return 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands() != 1:
                        return 1
                    
                    grid[i][j] = 1
        
        return 2