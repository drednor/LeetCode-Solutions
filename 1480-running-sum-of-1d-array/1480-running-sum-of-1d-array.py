class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if i > 0:
                nums[i] += nums[i-1]
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