class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for idx in range(1, len(prices)):
            cur = prices[idx]
            max_profit = max(max_profit, cur - min_price)
            min_price = min(min_price, cur)
        
        return max_profit
        