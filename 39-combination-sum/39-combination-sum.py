class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def sumsub(i, total, nums):
            if total>target or i >= len(candidates):
                return
            if total == target:
                result.append(nums.copy())
                return
            nums.append(candidates[i])
            sumsub(i, candidates[i]+total, nums)
            nums.pop()
            sumsub(i+1, total, nums)
            return 
        sumsub(0,0,[])
        return result