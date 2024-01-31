class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        ans = [0]*len(temperatures)
        for cur, cur_temp in enumerate(temperatures):
            while stack and cur_temp > temperatures[stack[-1]]:
                ans[stack[-1]] = cur - stack[-1]
                stack.pop()
            
            stack.append(cur)
        
        
        return ans
            