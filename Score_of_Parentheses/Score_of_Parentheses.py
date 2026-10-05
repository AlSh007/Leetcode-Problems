class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack, cur = [], 0

        for char in s:
            if char == '(':
                stack.append(cur)
                cur = 0
            else:
                cur += stack.pop() + max(cur, 1)
        
        return cur