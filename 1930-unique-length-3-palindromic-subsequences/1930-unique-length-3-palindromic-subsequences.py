class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        
        for mid_char in string.ascii_lowercase:
            first, last = s.find(mid_char), s.rfind(mid_char)
            if first > -1:
                res += len(set(s[first + 1:last]))
            
        
        return res