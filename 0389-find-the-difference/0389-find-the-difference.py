class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        i, j = 0, 0
        while i< len(s) and j <len(t):
            if s[i] != t[j]:
                return t[j]
            i += 1
            j += 1
        return t[-1]