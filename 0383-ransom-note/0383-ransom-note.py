class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        st1 = Counter(ransomNote)
        st2  = Counter(magazine)
        
        return st1 & st2 == st1 