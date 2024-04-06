class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = [] #to mark indices of opening parantheses
        s = list(s)
        
        for i, char in enumerate(s):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        while stack:
            s[stack.pop()] = ''
        
        return ''.join(s)