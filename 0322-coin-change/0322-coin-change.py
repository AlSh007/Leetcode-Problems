class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def helper(amount,i):
            if amount == 0:
                return 0
            if i == -1:
                return math.inf
            
            ans = helper(amount, i-1)
            if coins[i] <= amount:
                ans = min(ans, helper(amount - coins[i], i) + 1)
            return ans
        n = len(coins)
        ans = helper(amount, n-1)
        return ans if ans != math.inf else -1