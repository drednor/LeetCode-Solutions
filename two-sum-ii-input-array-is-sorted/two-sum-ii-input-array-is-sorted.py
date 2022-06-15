class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        somemap = {}
        for i, n in enumerate(numbers):
            if (target-n) in somemap:
                return [somemap[target-n]+1,i+1]
            somemap[n] = i
        return 