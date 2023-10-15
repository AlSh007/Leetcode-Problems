class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        memo = {}
        
        def dp(step, index):
            if step == 0:
                return 1 if index == 0 else 0
            if index < 0 or index >= arrLen or step < 0:
                return 0
            if (step, index) in memo:
                return memo[(step, index)]
            
            ways = dp(step - 1, index)%MOD #we stay
            ways += dp(step - 1, index - 1)%MOD #we go left
            ways += dp(step - 1, index + 1)%MOD #we go right
            memo[(step, index)] = ways%MOD
            return memo[(step, index)]
        
        return dp(steps, 0)