
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        result = 1
        for i in nums:
            if i == 0:return 0
            if i < 0 : result *= -1
        return result
    
    