class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # table = [0] * (len(cost))
        # table[0] = cost[0]
        # table[1] = cost[1]
        for i in range(len(cost)):
            if i+2<len(cost):
                cost[i+2] += min(cost[i],cost[i+1])
        return min(cost[-1], cost[-2])
        
#         memo = {}
#         def recur(i):
#             if i in memo:
#                 return memo[i]
#             if i == len(cost)-1:
#                 return cost[-1]
#             if i == len(cost)-2:
#                 return cost[-2]
#             memo[i] = cost[i] + min(recur(i+1) if i < (len(cost)-1) else 1000 ,recur(i+2) if i < (len(cost)-2) else 1000)
#             return memo[i]
#         return min(recur(0), recur(1))
                
             
            
            
        