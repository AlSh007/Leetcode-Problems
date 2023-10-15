class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        arrLen = min(arrLen, steps //2 + 1)
        
        dp = [0]*arrLen
        
        prevDp = [0]*arrLen
        
        prevDp[0] = 1
        
        
        for step in range(1, steps + 1):
            dp = [0]*arrLen
            for index in range(arrLen - 1, -1, -1): #becuase our answer state is index = 0 that's why we are going in reverse
                ans = prevDp[index]
                
                if index > 0:
                    ans = (ans + prevDp[index - 1]) %MOD
                
                if index < arrLen - 1:
                    ans = (ans +  prevDp[index + 1])%MOD
                    
                dp[index] = ans
            
            prevDp = dp
        
        return dp[0]