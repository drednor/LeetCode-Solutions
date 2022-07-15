from collections import Counter
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        par = [i for i in range(len(isConnected)+1)]
        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(n1,n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return False
            else:
                par[p1] = p2
            return True
        
        res = len(isConnected)
        for i in range(len(isConnected)):
            for j in range(i+1,len(isConnected)):
                    if isConnected[i][j] == 1:
                        if union(i+1, j+1):
                            res -= 1             
        return res
            
        