class Solution:
    mod = 10**9 + 7
    
    def recursion(self, dp, n, k, target):
        if target == 0 and n == 0:
            return 1
        if n == 0 or target <= 0:
            return 0
        
        if dp[n][target] != -1:
            return dp[n][target]
        
        ways = 0
        for i in range(1, k + 1):
            ways = (ways + self.recursion(dp, n - 1, k, target - i)) % self.mod
        
        dp[n][target] = ways %self.mod
        return dp[n][target]
        
        
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[-1]*(target + 1) for _ in range(n + 1)]
        return self.recursion(dp, n, k, target)