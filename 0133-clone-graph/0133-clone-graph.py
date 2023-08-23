"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        
        q, clones = deque([node]), {node.val : Node(node.val,[])}
        while(q):
            cur = q.popleft()
            cur_clone = clones[cur.val]
            
            for ngh in cur.neighbors:
                if ngh.val not in clones:
                    clones[ngh.val] = Node(ngh.val,[])
                    q.append(ngh)
                
                cur_clone.neighbors.append(clones[ngh.val])
        return clones[node.val]
