class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            #at each step
            #track min price for buying
            #track max profit for selling
            min_price = min(prices[i],min_price)
            max_profit = max(max_profit, (prices[i] - min_price))

        return max_profit