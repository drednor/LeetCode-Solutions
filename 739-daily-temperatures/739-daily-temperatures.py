class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        
        for i , t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, idx = stack.pop()
                res[idx] = i - idx
            stack.append([t, i])
        return res
            
        
        # ITERATIVE SOLUTION O(n^2)
        # result = [0] * len(temperatures)
        # for i in range(len(temperatures)):
        #     for j in range(i+1,len(temperatures)):
        #         if i == j:
        #             continue
        #         if temperatures[j]>temperatures[i]:
        #             result[i] = j-i
        #             break
        #         result[i] = 0
        # return result
        