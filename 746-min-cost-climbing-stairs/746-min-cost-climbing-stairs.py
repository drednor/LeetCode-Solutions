class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        result = 0
        table = [0] * (len(cost))
        table[0] = cost[0]
        table[1] = cost[1]
        for i in range(len(table)):
            if i+2<len(cost):
                table[i+2] += cost[i+2] + min(table[i],table[i+1])
        return min(table[-1], table[-2])
                
             
            
            
        