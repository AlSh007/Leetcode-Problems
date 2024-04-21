class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
            
        def dfs(node, visited):
            if node == destination:
                return True
            if node in visited:
                return False
            
            visited.add(node)
            
            for neigh in graph[node]:
                if dfs(neigh, visited):
                    return True
            
            return False
        
        visited = set()
        return dfs(source, visited)