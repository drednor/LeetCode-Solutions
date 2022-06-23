class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and postfix
        result = [1] * len(nums)
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            result[i]*= postfix
            postfix*=nums[i]
        return result
        
        
        
        
        # result = [0] * len(nums)
        # count = 1
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j:
        #             count *= nums[j]
        #     result[i] = count
        #     count = 1
        # return result