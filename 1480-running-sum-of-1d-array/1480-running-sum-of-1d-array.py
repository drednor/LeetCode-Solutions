class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp = 0
        res = []
        for i in range(len(nums)):
            temp += nums[i]
            nums[i] = temp
        return nums
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Using the same list 
#         for i in range(len(nums)):
#             if i>0:
#                 nums[i] = nums[i] + nums[i-1] 
#         return nums
        
        # #creating a new list
        # result = [0] * len(nums)
        # for i in range(len(nums)):
        #     result[i] = sum(nums[:i+1])
        # return result