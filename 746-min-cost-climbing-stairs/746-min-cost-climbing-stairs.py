class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # table = [0] * (len(cost))
        # table[0] = cost[0]
        # table[1] = cost[1]
        for i in range(len(cost)):
            if i+2<len(cost):
                cost[i+2] += min(cost[i],cost[i+1])
        return min(cost[-1], cost[-2])
                
             
            
            
        