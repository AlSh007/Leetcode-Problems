class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        count = 1

        #simple idea is to build build every number n using all the perfect squares. Initially, we start with 1, then we move on to the next perfect square, which is 4, then we move on to 9, and so on. 
        while count * count <= n:
            sq = count * count
            for i in range(sq, n + 1):
                dp[i] = min(dp[i - sq] + 1, dp[i])
            
            count += 1
        
        return dp[n]
