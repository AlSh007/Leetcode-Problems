class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def answer(curr: str,val: float):
            if curr == self.dst:
                return val
            for adj, adj_val in self.graph[curr].items():
                if adj not in self.seen:
                    self.seen.add(adj)
                    result = answer(adj, val*adj_val)
                    if result!=-1:
                        return result
                    self.seen.remove(adj)
            return -1
                    
            
            
        self.graph = defaultdict(dict)
        self.seen = set()
        for (a , b), val in zip(equations, values):
            self.graph[a][b] = val
            self.graph[b][a] = 1/val
        result = []
        for src, self.dst in queries:
            result.append(answer(src , 1) if src in self.graph else -1)
            self.seen.clear()
            
        return result