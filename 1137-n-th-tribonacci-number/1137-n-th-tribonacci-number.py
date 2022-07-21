class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return n
        if n == 1:
            return 1
        table = [None] * (n+1)
        table[0] = 0
        table[1] = 1
        table[2] = 1
        for i in range(len(table)):
            if i+3<len(table):
                table[i+3] = table[i+2] + table[i+1] + table[i]
        return table[n]
        