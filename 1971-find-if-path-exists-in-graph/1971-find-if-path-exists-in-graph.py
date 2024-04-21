class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = list(range(n))
        
        rank = [1]*n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            
            return parent[x]
        
        def union(x, y):
            parX = find(x)
            parY = find(y)
            
            if parX != parY:
                if rank[parX] > rank[parY]:
                    parent[parY] = parX
                elif rank[parY] > rank[parX]:
                    parent[parX] = parY
                else:
                    parent[parY] = parX
                    rank[parX] += 1
                    
        for u, v in edges:
            union(u, v)
        
        return find(source) == find(destination)