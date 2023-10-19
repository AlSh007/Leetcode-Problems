class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def getString(s):
            count = 0
            res = ''
            for char in s[::-1]:
                if char == '#':
                    count += 1
                else:
                    if count > 0:
                        count -= 1
                    else:
                        res += char
            return res
        
        return getString(s) == getString(t) 