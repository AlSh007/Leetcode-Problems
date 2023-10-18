class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        inDegree = [0]*(n)
        
        for parent, child in relations:
            parent, child = parent - 1, child - 1 # convert into zero-based index
            inDegree[child] += 1
            graph[parent].append(child)
        
        queue = deque()
        max_time = [0]*n
        
        for node in range(n):
            if inDegree[node] == 0:
                queue.append(node)
                max_time[node] = time[node]
       
        
        while queue:
            node = queue.popleft()
            for neigh in graph[node]:
                max_time[neigh] = max(max_time[neigh], max_time[node] + time[neigh])
                inDegree[neigh] -= 1
                if inDegree[neigh] == 0:
                    queue.append(neigh)

        return max(max_time)
                