class Solution:
    def maxLength(self, arr: List[str]) -> int:
        unique = []
        
        for s in arr:
            u = set(s)
            if len(s) == len(u):
                unique.append(u)
        
        concat = [set()]
        
        for u in unique:
            for c in concat:
                if not c & u:
                    concat.append( c | u )
        
        return max(len(cc) for cc in concat)