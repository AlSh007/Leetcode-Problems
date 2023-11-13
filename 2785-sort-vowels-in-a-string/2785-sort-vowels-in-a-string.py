class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        sortMe = [ c for c in s if c in vowels ]
        sortMe.sort(reverse=True)
        stringBuilder = [ sortMe.pop() if c in vowels else c for c in s ]
        return "".join(stringBuilder)