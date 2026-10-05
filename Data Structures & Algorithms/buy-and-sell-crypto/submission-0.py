class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        buy = prices[l]
        profit = 0

        for r in range(1, len(prices)):
            if buy > prices[r]:
                buy = prices[r]
            
            profit = max(profit, prices[r] - buy)

        return profit