class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def checkVowels(s):
            ans = 0
            for i in s.lower():
                if i in ['a','e','i','o','u']:
                    ans += 1
            return ans
        
        count1 = checkVowels(s[:len(s)//2])
        count2 = checkVowels(s[len(s)//2:])
        
        return count1 == count2