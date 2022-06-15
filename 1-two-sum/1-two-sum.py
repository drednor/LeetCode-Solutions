class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        somemap ={}
        result = [] 
        for i , n in enumerate(nums):
            if (target-n) in somemap:
                return [somemap[target-n],i]
            somemap[n] = i
        return
        