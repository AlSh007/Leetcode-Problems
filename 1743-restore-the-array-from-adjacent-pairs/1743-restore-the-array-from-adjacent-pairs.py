class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for x, y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)
        
        root = None
        
        for node in graph:
            if len(graph[node]) == 1:
                root = node
                break
                
        ans = []
        
        def dfs(node, prev):
            ans.append(node)
            for neighbor in graph[node]:
                if neighbor != prev:
                    dfs(neighbor, node)
        
        dfs(root,None)
        return ans
        
        
        
        