class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n < 2:
            return 1
        component_count = 0
        graph = defaultdict(list)
        indegree = [0 for _ in range(n)]
        
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            indegree[node1] += 1
            indegree[node2] += 1
        
        queue = deque(node for node in range(n) if indegree[node] == 1)
        
        while queue:
            current_node = queue.popleft()
            indegree[current_node] -= 1
            add_value = 0
            
            if values[current_node] % k == 0:
                component_count += 1
            else:
                add_value = values[current_node]
            
            for neighbor_node in graph[current_node]:
                if indegree[neighbor_node] == 0:
                    continue
                indegree[neighbor_node] -= 1
                values[neighbor_node] += add_value
                
                if indegree[neighbor_node] == 1:
                    queue.append(neighbor_node)
        
        return component_count
        