class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        
        def dfs(i, amt):
            if amt == amount:
                return 1
            
            if amt > amount or i == len(coins):
                return 0
            
            if (i, amt) in cache:
                return cache[(i, amt)]
            
            cache[(i, amt)] = dfs(i + 1, amt) + dfs(i, amt + coins[i])
            return cache[(i, amt)]
        
        return dfs(0, 0)