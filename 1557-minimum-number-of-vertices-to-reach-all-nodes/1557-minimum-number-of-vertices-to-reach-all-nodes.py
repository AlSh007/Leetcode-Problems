class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        set1=set(range(n))
        set2=set(j for i,j in edges)
        return list(set1-set2)