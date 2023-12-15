class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        has_outgoing = set()
        for i in range(len(paths)):
            has_outgoing.add(paths[i][0])
        
        for i in range(len(paths)):
            if paths[i][1] not in has_outgoing:
                return paths[i][1]
        
        return ""