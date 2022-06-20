class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0, 1
        max_p = 0 
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_p = max(profit, max_p)
            else: 
                l = r
            r += 1
        return max_p
            
        
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         if prices[j] - prices[i] > max_profit:
        #             max_profit = prices[j] - prices[i]
        # return max_profit
                    
        