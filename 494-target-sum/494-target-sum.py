class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def recur(i, total):
            key = (i,total)
            if i == len(nums):
                return 1 if total == target else 0
            if key in memo:
                return memo[key]
            plus = recur(i+1,total+nums[i])
            minus = recur(i+1, total-nums[i])
            memo[key] = plus + minus 
            return memo[key]
        return recur(0,0)