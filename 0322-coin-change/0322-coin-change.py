class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dp(amount):
            if amount == 0:
                return 0
            
            
            ans = math.inf
            for coin in coins:
                if coin <= amount:
                    ans = min(ans, dp(amount - coin) + 1)
            return ans
    
        ans = dp(amount)
        return ans if ans != math.inf else -1