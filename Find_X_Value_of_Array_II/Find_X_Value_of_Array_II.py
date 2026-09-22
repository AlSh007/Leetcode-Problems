class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> 
    List[int]:
        class Node:
            __slots__ = ('prod', 'freq')
            def __init__(self):
                self.prod = 1
                self.freq = [0] * k
        
        n = len(nums)
        tree = [Node() for _ in range(4 * n)]
        
        def merge(L: Node, R: Node) -> Node:
            res = Node()
            res.prod = (L.prod * R.prod) % k
            res.freq = L.freq[:]
            for r in range(k):
                if R.freq[r]:
                    nr = (L.prod * r) % k