class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = prev = 0
        for i in range(1, len(colors)):
            if colors[prev] != colors[i]:
                prev = i
            else:
                res += min(neededTime[i], neededTime[prev])
                if neededTime[prev]< neededTime[i]:
                    prev = i
        return res
        
        
        # n = len(colors)
        # prev = (None, None)
        # i = 0 
        # res = 0
        # while i < n:
        #     pc, pt = prev
        #     if colors[i] == pc:
        #         if neededTime[i] >= pt:
        #             res += pt
        #         else:
        #             res += neededTime[i]
        #             i+=1
        #             continue
        #     prev = (colors[i],neededTime[i])
        #     i+=1
        # return res
                    
                
                    