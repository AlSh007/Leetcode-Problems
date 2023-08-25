class Solution:
    def findMinHeightTrees(self, n: int, E: List[List[int]]) -> List[int]:
        if not E:
            return [0]
        G, seen = defaultdict(set), [False]*n
        for u, v in E:
            G[u].add(v)
            G[v].add(u)
        
        leaves, new_leaves, indegree = [], [], []
        for i in range(n):
            if len(G[i]) == 1:
                leaves.append(i)
            indegree.append(len(G[i]))
        
        while n > 2:
            for leaf in leaves:
                for adj in G[leaf]:
                    indegree[adj] -= 1
                    if indegree[adj] == 1:
                        new_leaves.append(adj)
            n -= len(leaves)
            leaves = new_leaves[:]
            new_leaves.clear()
            
        return leaves
        