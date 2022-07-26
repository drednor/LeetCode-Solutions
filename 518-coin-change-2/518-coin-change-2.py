class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        table = [[0]*(amount+1) for _ in range(len(coins)+1)]
        table[0][0] = 1
        for j , coin in enumerate(coins):
            table[j+1][0] = 1
            for i in range(1,len(table[0])):
                if i-coin >= 0:
                    table[j+1][i] = table[j+1][i-coin] + table[j][i]
                else:
                    table[j+1][i] += table[j][i]
        return table[-1][-1]
        
        # memo = {}
        # result = [0]
        # def recur(total,i):
        #     key = total,i
        #     if key in memo:
        #         return memo[key]
        #     if total == 0:
        #         return 1
        #     if i >= len(coins):
        #         return 0
        #     coin = coins[i]
        #     res = 0
        #     for num in range((total//coin)+1):
        #         rem = total - (num*coin)
        #         #print(rem, coin ,total)
        #         res += recur(rem,i+1)
        #     memo[key] = res
        #     return memo[key]
        # return recur(amount,0)