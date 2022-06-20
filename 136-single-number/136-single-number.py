class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = {}
        for i in nums:
            result[i] = 1 + result.get(i,0) 
        return (list(result.keys())[list(result.values()).index(1)])