class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = None
        for i in nums:
            if result is None:
                result = i
            if i < result:
                result = i
                
        return result