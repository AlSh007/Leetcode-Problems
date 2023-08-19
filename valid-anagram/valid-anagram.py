class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)
        
        for char in s:
            count[char] += 1
        
        for char in t:
            count[char] -= 1
            
        for val in count.values():
            if val != 0:
                return False
        
        return True