class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        result = 0
        for i in range(len(nums)):
            if nums[i] != 1:
                result = 0
            else:
                result += 1
            ans = max(ans,result)
        return ans