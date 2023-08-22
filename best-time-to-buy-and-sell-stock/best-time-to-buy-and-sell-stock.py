class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res , minEl = 0, inf
        n = len(prices)
        for price in prices:
            minEl = min(minEl,price)
            res = max(res,price - minEl)
        return res