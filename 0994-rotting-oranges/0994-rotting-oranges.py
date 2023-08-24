class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        q = deque()
        fresh_count = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        time_passed = 0
        while q and fresh_count > 0:
            time_passed += 1
            
            for i in range(len(q)):
                x, y = q.popleft()
                for dx, dy in ((x-1,y), (x, y-1), (x+1,y), (x, y+1)):
                    if dx < 0 or dx >= rows or dy >= cols or dy < 0:
                        continue
                    if grid[dx][dy] != 1:
                        continue
                    fresh_count -= 1
                    grid[dx][dy] = 2
                    q.append((dx, dy))
                    
        return time_passed if fresh_count == 0 else -1
            