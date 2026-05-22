class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 1000
        max_profit = 0
        for price in prices:
            if price < lowest:
                lowest = price
            day_profit = price - lowest

            if day_profit > max_profit:
                max_profit = day_profit
        
        return max_profit