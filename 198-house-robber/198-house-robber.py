class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.insert(0,0)
        for i in range(len(nums)):
            if i+3<len(nums):
                nums[i+3] += max(nums[i],nums[i+1])
        return max(nums[-1],nums[-2])
        
        
        
        # memo = {}
        # def recur(i):
        #     if i in memo:
        #         return memo[i]
        #     if i >= len(nums):
        #         return 0
        #     left = nums[i] + recur(i+2)
        #     right = recur(i+1)
        #     memo[i] = max(left,right)
        #     return memo[i]
        # return recur(0)