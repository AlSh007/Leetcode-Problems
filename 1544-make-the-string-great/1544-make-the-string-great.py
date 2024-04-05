class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for char in s:
            if stack and char == stack[-1].swapcase():
                stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack)