class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s)%2:
            return False
        brackets = {'(':')', '{':'}', '[':']'}
        for char in s:
            if char in brackets:
                stack.append(char)
            elif not stack or brackets[stack.pop()] != char:
                return False
        return True if len(stack) == 0 else False