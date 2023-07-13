class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses <= 0:
            return False
        inDegree = {i : 0 for i in range(numCourses)}
        graph = {i : [] for i in range(numCourses)}
        
        for child, parent in prerequisites:
            graph[parent].append(child)
            inDegree[child] += 1

        sources = deque()
        
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)
        visited = 0       
        while sources:
            vertex = sources.popleft()
            visited += 1
            for child in graph[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)
        
        return visited == numCourses