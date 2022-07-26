class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def recur(i, flag):
            key = (i, flag)
            if key in memo:
                return memo[key]
            if i >= len(prices):
                return 0 
            if flag:
                buy = recur(i+1,False) - prices[i]
                cd = recur(i+1,True)
                memo[key] = max(buy,cd)    
            else:
                sell = recur(i+2,True) + prices[i] 
                cd = recur(i+1,False)
                memo[key] = max(sell,cd)
            return memo[key]
        return recur(0,True)
        