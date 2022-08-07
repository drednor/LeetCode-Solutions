class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # table = [[], [1,1,1,1,1]]
        # a,e,i,o,u = 0,1,2,3,4
        # mod = (10**9) + 7
        # for j in range(2, n+1):
        #     table.append([0,0,0,0,0])
        #     table[j][a] = table[j-1][e] + table[j-1][i] + table[j-1][u] % mod
        #     table[j][e] = table[j-1][a] + table[j-1][i] % mod
        #     table[j][i] = table[j-1][e] + table[j-1][o] % mod
        #     table[j][o] = table[j-1][i]
        #     table[j][u] = table[j-1][i] + table[j-1][o] % mod
        # return sum(table[n]) % mod
        
        a,e,i,o,u = 1,1,1,1,1
        for _ in range(n-1):
            a,e,i,o,u = e + i + u , a + i, e + o,i,i + o
        return (a+e+i+o+u) % ((10**9)+7)
                
            