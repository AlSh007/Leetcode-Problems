#User function Template for python3

from typing import List
from queue import Queue
from collections import defaultdict, deque
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        graph = defaultdict(list)
        for u, v in enumerate(adj):
            for i in v:
                graph[u].append(i)
                
        q = deque([0])
        visited = [0]*V
        visited[0] = 1
        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            for neighbor in graph[node]:
                if visited[neighbor] != 1:
                    visited[neighbor] = 1
                    q.append(neighbor)
        
        return ans


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends