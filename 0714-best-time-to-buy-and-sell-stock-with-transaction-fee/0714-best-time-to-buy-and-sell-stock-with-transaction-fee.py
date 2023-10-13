class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        buy, sell = -prices[0], 0 #if we buy and sell on first day
        
        for i in range(1,n):
            buy = max(buy,sell-prices[i]) #profiit from buying will be last sell profit - today's stock price
            sell = max(sell,buy+prices[i]-fee) #profit if we sell today
        
        return sell #gotta sell finally cant hold the stock