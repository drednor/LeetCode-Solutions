class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binsearch(nums,target, True)
        right = self.binsearch(nums, target, False)
        return [left,right]
    
    
    def binsearch(self,nums, target, leftbias):
        l , r = 0 , len(nums)-1
        i = -1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]> target:
                r = mid -1
            elif nums[mid]< target:
                l = mid+1
            else:
                i = mid
                if leftbias:
                    r = mid-1
                else:
                    l = mid+1
        return i 
            
            
        
        
        
        # ITERATIVE SOLUTION
        # result = [-1,-1]
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         result[0] = i
        #         break
        # else:
        #     return result
        # for i in range(len(nums)-1, -1,-1):
        #     if nums[i] == target:
        #         result[1] = i
        #         break
        # return result
        