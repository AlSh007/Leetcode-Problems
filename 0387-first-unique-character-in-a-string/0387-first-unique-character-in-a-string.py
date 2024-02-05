class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        seen = set()
        for idx, char in enumerate(s):
            if char not in seen:
                d[char] = idx
                seen.add(char)
            elif char in d:
                del d[char]
        return min(d.values()) if d else -1
            