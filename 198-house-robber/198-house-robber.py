class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return max(nums[0],nums[1])
        memo = {}
        def recur(i):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0
            left = nums[i] + recur(i+2)
            right = recur(i+1)
            memo[i] = max(left,right)
            return memo[i]
        return recur(0)