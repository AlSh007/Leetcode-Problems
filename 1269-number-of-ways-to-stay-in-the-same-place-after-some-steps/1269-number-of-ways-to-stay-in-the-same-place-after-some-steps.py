class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        arrLen = min(arrLen, steps //2 + 1)
        
        dp = [[0]*(steps + 1) for _ in range(arrLen)]
        
        dp[0][0] = 1
        
        for step in range(1, steps + 1):
            for index in range(arrLen - 1, -1, -1):
                ans = dp[index][step - 1]
                
                if index > 0:
                    ans = (ans + dp[index - 1][step - 1]) %MOD
                
                if index < arrLen - 1:
                    ans = (ans +  dp[index + 1][step - 1])%MOD
                    
                dp[index][step] = ans
        
        return dp[0][steps]