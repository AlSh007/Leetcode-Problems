class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = list(range(n))
        size = [1]*n
        
        def find_parent(a):
            if parent[a] != a:
                parent[a] = find_parent(parent[a])
            
            return parent[a]
        
        def union(a, b):
            pa = find_parent(a)
            pb = find_parent(b)
            
            if pa == pb:
                return
            pbig, psmall = (pa, pb) if size[pa] > size[pb] else (pb, pa)
            size[pbig] += psmall
            parent[psmall] = pbig
        
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    union(i, j)
        
        return len(set(find_parent(i) for i in range(n)))