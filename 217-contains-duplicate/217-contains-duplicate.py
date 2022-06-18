class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = {}
        for i in nums:
            result[i] = result[i]+1 if i in result else 1
            if result[i]>1:
                return True
        return False
        
        