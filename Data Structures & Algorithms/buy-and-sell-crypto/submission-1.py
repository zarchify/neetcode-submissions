class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_seen = 0

        for i, price in enumerate(prices):
            if prices[min_seen] > price:
                min_seen = i
            max_profit = max(max_profit, price - prices[min_seen])
            print(max_profit)

            

 

        return max_profit