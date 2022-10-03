class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        prev = (None, None)
        i = 0 
        res = 0
        while i < n:
            pc, pt = prev
            if colors[i] == pc:
                if neededTime[i] >= pt:
                    res += pt
                else:
                    res += neededTime[i]
                    i+=1
                    continue
            
            prev = (colors[i],neededTime[i])
            i+=1
        return res
                    
                
                    