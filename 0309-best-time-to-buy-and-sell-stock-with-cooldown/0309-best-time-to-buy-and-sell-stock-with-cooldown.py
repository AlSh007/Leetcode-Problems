class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cool_down, sell, hold = 0, 0, -float('inf')
        
        for current_stock_price in prices:
            prev_cool_down, prev_sell, prev_hold = cool_down, sell, hold
            
            cool_down = max(prev_cool_down, prev_sell)
            
            sell = current_stock_price + prev_hold
            
            hold = max(prev_hold, prev_cool_down - current_stock_price)
            
        return max(sell, cool_down)
            