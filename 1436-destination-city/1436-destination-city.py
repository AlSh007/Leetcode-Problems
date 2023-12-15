class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        journey = { f:t for f,t in paths}
        
        path = paths[0][0]
        
        while path in journey:
            path = journey[path]
        
        return path