class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        
        def calc(i, j):
            if j - i < 2:
                return 0
            if i + 1 == j or dp[i][j] != -1:
                return dp[i][j]
            
            coins = 0
            for ind in range(i+1, j):
                coins = max(coins, nums[i]*nums[ind]*nums[j] + calc(i,ind)+ calc(ind, j))
            dp[i][j] = coins
            return dp[i][j]
            
        
        
        n = len(nums)
        dp = [[-1]*(n) for _ in range(n)]
        return calc(0, n - 1)
        