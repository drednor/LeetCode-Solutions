class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = 0
        start = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                start = i+1
        return start
        #         def check(start):
#             index = start+1
#             if index == len(cost):
#                 index = 0
#             tank = gas[start]
#             while index != start:
#                 tank = tank + gas[index] - cost[index-1]
#                 index+=1
#                 if index == len(cost):
#                     index = 0
#                 if tank < cost[index-1]:
#                     return False
#             return True
                
#         for i in range(len(gas)):
#             if gas[i] < cost[i]:
#                 continue
#             if check(i):
#                 return i
#         return -1
                