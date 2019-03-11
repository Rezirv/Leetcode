class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        maxProfit = 0
        for i in range(1, length):
            minstock = min(prices[:i])
            if maxProfit < (prices[i] - minstock):
                maxProfit = prices[i] - minstock
        return maxProfit


