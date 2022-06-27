class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        first , second = [0]*26, [0]*26
        for i in range(len(s1)):
            first[ord(s1[i])- ord('a')] += 1
            second[ord(s2[i])- ord('a')] += 1
        matches = 0
        for i in range(26):
            matches += (1 if first[i]== second[i] else 0)
            
        l = 0 
        for r in range(len(s1),len(s2)):
            if matches == 26: return True
            
            index = ord(s2[r]) - ord('a')
            second[index] += 1
            if first[index] == second[index]:
                matches += 1
            elif first[index]+1 == second[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            second[index] -= 1
            if first[index] == second[index]:
                matches += 1
            elif first[index]-1 == second[index]:
                matches -= 1
            
            l+=1
        return matches == 26
            
        
        
        # WRONG SOLUTION FOR HASHMAPS
        # first = dict.fromkeys(string.ascii_lowercase, 0)
        # second = dict.fromkeys(string.ascii_lowercase, 0)
        # for i in range(len(s1)):
        #     first[s1[i]] = 1+ first.get(s1[i],0) 
        #     second[s2[i]] = 1+ second.get(s2[i], 0)
        # matches = 0
        # for k,v in first.items():
        #     matches += 1 if first[k] == second[k] else 0
        # l = 0
        # for r in range(len(s1), len(s2)):
        #     if matches == 26: return True
        #     second[s2[r]] = 1+second.get(s2[r], 0)
        #     if first[s2[r]] == second[s2[r]]:
        #         matches +=1
        #     else:
        #         matches -= 1
        #     if first[s2[l]] == second[s2[l]]:
        #         matches +=1
        #     else:
        #         matches -= 1
        #     l+=1
        # return matches == 26
                
            
            
                
        
        # c = Counter(s1)
        # l, r = 0 , len(s1)-1
        # while r<len(s2):
        #     temp = Counter(s2[l:r+1])
        #     if temp == c:
        #         return True
        #     r+=1
        #     l+=1
        # return False
        