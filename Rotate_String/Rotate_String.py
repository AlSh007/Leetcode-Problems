class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
            
        new_string = s + s

        return new_string.find(goal) != -1