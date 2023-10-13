class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        hold, free = -prices[0], 0
        
        for i in range(1,n):
            hold = max(hold,free-prices[i])
            free = max(free,hold+prices[i]-fee)
        
        return free