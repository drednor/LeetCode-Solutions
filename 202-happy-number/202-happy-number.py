class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        def recur(num):
            if num == 1:
                return True
            if num in s:
                return False
            s.add(num)
            total = 0
            for char in str(num):
                total += int(char)**2
            if recur(total):
                return True
            else:
                return False
            return False
        return recur(n)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # seen = set()
        # while n!=1:
        #     n = sum([int(i)**2 for i in str(n)])
        #     if n in seen:
        #         return False
        #     else:
        #         seen.add(n)
        # else:
        #     return True