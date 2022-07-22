class Solution:
    def rob(self, nums: List[int]) -> int:
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