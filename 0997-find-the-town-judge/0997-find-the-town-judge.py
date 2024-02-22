class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_map = [0]*(n+1)
        
        for a, b in trust:
            trust_map[a] -= 1
            trust_map[b] += 1
        
        for i in range(1, n + 1):
            if trust_map[i] == n - 1:
                return i
        
        return -1