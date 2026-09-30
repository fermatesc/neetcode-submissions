class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return  max(max(prices[i:]) - p for i, p in enumerate(prices)  )