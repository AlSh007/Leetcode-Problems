class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowelsCount=0
        maxCount=0
        vowels="aeiou"
        for i,v in enumerate(s):
            if i>=k:
                if s[i-k] in vowels:
                    vowelsCount-=1
            if s[i] in vowels:
                    vowelsCount+=1
            maxCount=max(vowelsCount,maxCount)
        return maxCount