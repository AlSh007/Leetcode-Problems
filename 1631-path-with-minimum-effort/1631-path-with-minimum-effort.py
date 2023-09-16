class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        def isPath(effort):
            seen, dq = {(0,0)}, deque([(0,0)])
            while dq:
                x, y = dq.popleft()
                if x == len(heights) - 1 and y == len(heights[0]) - 1:
                    return True
                for dx, dy in ((x+1, y), (x, y+1), (x-1, y), (x, y-1)):
                    if 0<= dx <m and 0<=dy < n and abs(heights[dx][dy] - heights[x][y]) <= effort and (dx, dy) not in seen:
                        seen.add((dx, dy))
                        dq.append((dx, dy))
            
            return False
            
            
            
            
            
            
        low, hi = 0, 10**6
        while low < hi:
            effort = (low + hi ) >> 1
            if isPath(effort):
                hi = effort
                
            else:
                low = effort + 1
        
        return low