class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = {}
        
        def dfs(i, color):
            if i in colors:
                return colors[i] == color
            colors[i] = color
            for neigh in graph[i]:
                if not dfs(neigh, 1 - color):
                    return False
        
            return True
        
        
        for i in range(n):
            if i not in colors:
                if not dfs(i, 0):
                    return False
        
        return True
            