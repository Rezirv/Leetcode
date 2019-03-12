class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        length = len(prices)
        maxP = 0
        for i in range(1, length):
            if prices[i] > prices[i - 1]:
                maxP += prices[i] - prices[i - 1]
        return maxP
