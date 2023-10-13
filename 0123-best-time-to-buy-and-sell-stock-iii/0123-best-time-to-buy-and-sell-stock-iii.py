class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_first = float('-inf')
        sell_first = 0
        buy_second = float('-inf')
        sell_second = 0
        
        for price in prices:
            buy_first = max(buy_first, -price)
            sell_first = max(sell_first, buy_first + price)
            buy_second = max(buy_second, sell_first - price)
            sell_second = max(sell_second, buy_second + price)
        
        return sell_second