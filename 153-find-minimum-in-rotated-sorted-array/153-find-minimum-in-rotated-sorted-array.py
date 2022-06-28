class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0 , len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid]>nums[r]:
                l = mid +1
            else:
                r = mid 
        return nums[r]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         l , r = 0 , len(nums)-1
#         while l<r:
#             mid =(l+r)//2
#             if nums[r]<nums[mid]:
#                 l = mid+1
#             else:
#                 r = mid
#         return nums[l]
        
# #         result = None
# #         for i in nums:
#             if result is None:
#                 result = i
#             if i < result:
#                 result = i
                
#         return result