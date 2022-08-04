class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        if q == p:
            return 1
        # print(q/p)
        # if (q/p) > 0.5:
        #     res 
        # print(q)
        # temp = q
        
        while p%2 ==0 and q %2==0:
            p/=2
            q/=2
        
        if p%2 == 0 and q%2 == 1:
            return 2
        elif p%2 == 1 and q%2 == 0:
            return 0
        elif p%2 == 1 and q%2 ==1:
            return 1
        return -1
#         while temp <= p:
#             if temp == p:
#                 return 2
#             temp *= 2
        
#         temp = q
#         while temp <= p:
#             if temp == p:
#                 return 1
#             temp *= 3
#         return 0