class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in nums:
            if nums[j]!=i:
                j+=1
                nums[j] = i
        return j+1
                
                
        
        
        
        
        
        # j = 0
        # if len(nums) == 0: return 0
        # for i in range(1,len(nums)):
        #     if nums[j]<nums[i]:
        #         j+=1
        #         nums[j] = nums[i]
        # return j+1
                