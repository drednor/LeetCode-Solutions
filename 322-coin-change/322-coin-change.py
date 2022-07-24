class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = [None] * (amount+1)
        table[0] = 0
        for i in range(len(table)):
            if table[i] is not None:
                for coin in coins:
                    temp = i + coin
                    if temp < len(table):
                        shortest = table[i] + 1
                        if table[temp] is None or shortest < table[temp]:
                            table[temp] = shortest
        return table[amount] if table[amount] is not None else -1