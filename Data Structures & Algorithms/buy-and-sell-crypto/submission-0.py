class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        n = len(prices)
        if n <= 1:
            return 0

        profit = 0
        while j < n and i < n:
            if i > j:
                j += 1
            if prices[i] < prices[j]:
                if prices[j] - prices[i] > profit:
                    profit = prices[j] - prices[i]
            else:
                i = j
            j += 1
        return profit

        