class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        manhattan = lambda p1, p2 : abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        
        n = len(points)
        adj = defaultdict(list)
        
        for i in range(n):
            for j in range(i+1, n):
                dist = manhattan(points[i],points[j])
                adj[i].append((dist, j))
                adj[j].append((dist, i)) #makes the graph
                
        cnt , ans, visited, heap = 1, 0, [0]*n, adj[0]
        visited[0] = 1
        heapq.heapify(heap)
        
        while heap:
            dist, j = heapq.heappop(heap)
            if not visited[j]:
                visited[j], cnt, ans = 1, cnt + 1, ans + dist #adding the distance of the closest neighbour node
                for record in adj[j]:
                    heapq.heappush(heap, record) #adding the neighbours of the neighbouring node
                    
                if cnt >= n:
                    break
        return ans