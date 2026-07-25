class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyDay = 0
        # sellDay = 0
        profit = 0
        for i in range(len(prices)):
            if prices[i] < prices[buyDay]:
                buyDay = i
            if profit < prices[i] - prices[buyDay]:
                sellDay = i
                profit = prices[sellDay] - prices[buyDay]
        return profit

