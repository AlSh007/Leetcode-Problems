class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]*n
        count  = 0
        
        if not isConnected:
            return 0
        
        def dfs(idx):
            visited[idx] = True
            for i in range(n):
                if isConnected[idx][i]==1 and visited[i]==False:
                    visited[i] = True
                    dfs(i)
                    
        for idx in range(n):
            if visited[idx] == False:
                count+=1
                dfs(idx)
        
        return count