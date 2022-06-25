class Solution:
    def trap(self, height: List[int]) -> int:
        max_l = [None]*len(height)
        max_r = [None]*len(height)
        temp = 0
        for i in range(len(height)):
            max_l[i] = temp
            if temp <= height[i]:
                temp = height[i]
        temp = 0
        for j in range(len(height)-1,-1,-1):
            max_r[j] = temp
            if temp <= height[j]:
                temp = height[j]
        result = []
        for i in range(len(height)):
            if min(max_l[i],max_r[i]) >= height[i]:
                result.append(min(max_l[i],max_r[i]) - height[i])
        return sum(result)
        
            
        