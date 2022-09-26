class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parents = [i for i in range(26)]
        
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(a,b):
            ua = find(a)
            ub = find(b)
            
            parents[ua] = ub
            
        for equ in equations:
            if equ[1] == "!":
                continue
                
            a = ord(equ[0]) - ord("a")
            b = ord(equ[3]) - ord("a")
            union(a,b)
        
        for equ in equations:
            if equ[1] != "!":
                continue
            a = ord(equ[0]) - ord("a")
            b = ord(equ[3]) - ord("a")
            
            if find(a) == find(b):
                return False
        return True