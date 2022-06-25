class Solution:
    def trap(self, height: List[int]) -> int:
        #Time Complexity O(n) Space Complexity O(1)
        if not height: return 0
        l, r = 0 , len(height) -1
        leftmax = height[l]
        rightmax = height[r]
        result = 0
        while l <r:
            if leftmax<rightmax:
                l+=1
                leftmax = max(leftmax, height[l])
                result += leftmax - height[l]
            else:
                r-=1
                rightmax = max(rightmax, height[r])
                result += rightmax - height[r]
        return result
         
        
        # Time Complexity O(n) , Space Complexity O(n)
        # max_l = [None]*len(height)
        # max_r = [None]*len(height)
        # temp = 0
        # for i in range(len(height)):
        #     max_l[i] = temp
        #     if temp <= height[i]:
        #         temp = height[i]
        # temp = 0
        # for j in range(len(height)-1,-1,-1):
        #     max_r[j] = temp
        #     if temp <= height[j]:
        #         temp = height[j]
        # result = 0
        # for i in range(len(height)):
        #     if min(max_l[i],max_r[i]) >= height[i]:
        #         result += min(max_l[i],max_r[i]) - height[i]
        # return result
        
            
        