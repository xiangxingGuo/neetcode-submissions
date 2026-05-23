class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 # buy
        max_profit = 0

        for r in range(1, len(prices)): # sell
            if prices[l] > prices[r]: # negative profit
                l = r # change buy day
            else:
                max_profit = max(max_profit, prices[r] - prices[l])
        
        return max_profit