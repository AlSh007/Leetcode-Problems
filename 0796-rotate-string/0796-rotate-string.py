class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            s = list(s)
            new_string = s[1:]
            new_string.append(s[0])
            new_string = "".join(new_string)
            if new_string == goal:
                return True
            s = new_string
        
        return False