class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def recur(total):
            if total in memo:
                return memo[total]
            if total == 0:
                return 0
            if total < 0:
                return float("inf")
            shortest = float("inf")
            for coin in coins:
                rem = total - coin
                res = 1 + recur(rem)
                if res < shortest:
                    shortest = res
            memo[total] = shortest
            return shortest
        result = recur(amount)
        if result == float("inf"):
            return -1
        else:
            return result
                    
            
        
        
        
        
        
        # table = [None] * (amount+1)
        # table[0] = 0
        # for i in range(len(table)):
        #     if table[i] is not None:
        #         for coin in coins:
        #             temp = i + coin
        #             if temp < len(table):
        #                 shortest = table[i] + 1
        #                 if table[temp] is None or shortest < table[temp]:
        #                     table[temp] = shortest
        # return table[amount] if table[amount] is not None else -1