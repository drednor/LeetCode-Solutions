class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
        
         # Count Number of times a number is in array
#         result = {}
#         for i in nums:
#             result[i] = result[i]+1 if i in result else 1
#             if result[i]>1:
#                 return True
#         return False
        
        