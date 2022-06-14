class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        x = list(zip(s1,s2))
        result = 0
        for i in range(len(x)):
            if x[i][0] != x[i][1]:
                result+=1
        if result != 2:
            return False
        elif result == 2 and sorted(s1)==sorted(s2):
            return True
        else:
            return False
#         bad = []
        
#         for i in range(len(s1)):
#             if s1[i]!=s2[i]:
#                 bad.append(i)
        
#         if len(bad) !=2: return False
        
#         s1 = list(s1)
#         s1[bad[0]], s1[bad[1]] = s1[bad[1]],s1[bad[0]]
        
#         res = ""
        
#         for i in s1:
#             res += str(i)
        
#         return res == s2
        
                
        
        