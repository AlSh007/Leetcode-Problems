class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        efforts = [[math.inf]*n for _ in range(m)]
        efforts[0][0] = 0
        heap = [(0, 0, 0)]
        while heap:
            effort, x, y = heapq.heappop(heap)
            if (x, y) == (m-1, n-1):
                return effort
            for r, c in ((x+1, y), (x, y+1), (x-1, y), (x, y-1)):
                if m > r >= 0 <= c < n:
                    next_effort = max(effort, abs(heights[x][y] - heights[r][c]))
                    if efforts[r][c] > next_effort:
                        efforts[r][c] = next_effort
                        heapq.heappush(heap, (next_effort, r, c))