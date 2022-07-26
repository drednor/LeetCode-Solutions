class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # table = [None] * (amount+1)
        # table[0] = 0
        # for i in range(len(table)):
        #     if table[i] is not None:
        #         for coin in coins:
        #             temp = i + coin
        #             if temp < len(table):
        #                 if table[temp] is None:
        #                     table[temp] = 1
        #                 else:
        #                     table[temp] += table[i]  
        #         print(table)
        # return table[amount]        
    
        memo = {}
        result = [0]
        def recur(total,i):
            key = total,i
            if key in memo:
                return memo[key]
            if total == 0:
                return 1
            if i >= len(coins):
                return 0
            coin = coins[i]
            res = 0
            for num in range((total//coin)+1):
                rem = total - (num*coin)
                #print(rem, coin ,total)
                res += recur(rem,i+1)
            memo[key] = res
            return memo[key]
        return recur(amount,0)