class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        count = 0
        ans = 0
        for char in s:
            if char == '(':
                stack.append(char)
                count += 1
                ans = max(count, ans)
            elif char == ')':
                if stack[-1] == '(':
                    stack.pop()
                    count -= 1
        
        return ans
        