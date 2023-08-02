class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        idx = 0
        for ch in t:
            if idx < len(s):
                if ch == s[idx]:
                    idx += 1
            else:
                break
        return idx == len(s)