class Solution:
    def __init__(self):
        self.ans = 0
    
    def helper(self,start,count,indegree,requests,n):
        if start == len(requests):
            for i in range(n):
                if indegree[i]!=0:
                    return
            self.ans = max(self.ans,count)
            return
        
        indegree[requests[start][0]] -= 1
        indegree[requests[start][1]] += 1
        self.helper(start+1,count+1,indegree,requests,n)
        
        indegree[requests[start][0]] += 1
        indegree[requests[start][1]] -= 1
        self.helper(start+1,count,indegree,requests,n)
        
        
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        indegree = [0]*n
        self.helper(0,0,indegree,requests,n)
        return self.ans