class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
            
        
        q = deque([source])
        visited = set([source])
        
        while q:
            node = q.popleft()
            if node == destination:
                    return True
            
            for neigh in graph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    q.append(neigh)
            
        return False